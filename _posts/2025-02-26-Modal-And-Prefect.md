---
title: Running Custom Docker Images on Modal with Prefect Orchestration
date: 2024-10-12
author: Moishe Lettvin
---

I recently set up Prefect to use Modal as its dynamic worker pool, with a custom Docker image registered on ECR. There’s great documentation out there about setting up Prefect and Modal with a git repo, which covers many cases. In my case, I needed some custom installation and setup for the flow I’d be executing, which necessitated the custom Docker image. My organization already hosts Docker images on ECR, so using it for this workflow made sense.

I’ll going to walk through the specific steps with a toy application. I will assume you’ve already got a Modal account, a Prefect account, and an AWS account, and have set up all these services’ CLI tools and secrets on your local machine.
### Create an AWS Secret in Modal
This page [Private registries](https://modal.com/docs/guide/private-registries) has details. In short, create a Secret in Modal that contains `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_REGION`. You might also need `AWS_DEFAULT_REGION`. You’ll pass the name of this Secret as the `aws_secret` parameter in the deployment section of the `prefect.yaml` file below.
### Create a Modal Work Pool and Credential Block in Prefect
Follow the instructions on this page https://docs.prefect.io/v3/deploy/infrastructure-examples/serverless. This will walk you through creating the work pool and setting up the Modal credentials in Prefect to allow pushing.

Note that you should *not* specify an image or aws_secret in the work pool definition. We’ll specify that in the deployment, instead.
### Write a Simple Flow
Create a very simple `hello-world.py` flow, eg.
```
from prefect import flow

@flow(log_prints=True)
def my_flow():
    print("Hello, Modal!")
```

### Create a Dockerfile
Create a very simple Dockerfile that copies the directory containing your `hello-world.py`file into it and sets the working directory:
```
FROM prefecthq/prefect:3-latest

WORKDIR /opt/prefect
COPY . .
```
### Create a prefect.yaml file
This prefect.yaml file will create a Docker image based on the Dockerfile in your directory, with the flow in your hello-world.py as the entry point.

Things to note:
* Specify your aws id, aws region and ECR repository name in the `image_name`field in the `prefect_docker.deployments.steps.build_docker_image` section
* The `tag` used for your Docker image (specified in `build.prefect_docker.deployments.steps.build_docker_image`) must change on every deploy. This is because Modal caches images, and will not pick up a new image unless the `tag` or `image_name` has changed.
* Modal will fail if your images is built with `arm64` architecture (which happens by default if you’re building from an ARM Mac), so you need to specify `linux/x86_64` as your architecture
* The `job_variables.image` section should contain the full name (image name and tag) specified in the build section, as well as the Modal secret for AWS you created above. In this example, I called that secret `aws-secret` in Modal’s secret manager.

```
name: hello-world
prefect-version: 3.2.2

build:
- prefect_docker.deployments.steps.build_docker_image:
    id: build_image
    requires: prefect-docker>=0.3.1
    image_name: <your aws id>.dkr.ecr.<your aws region>.amazonaws.com/<your ecr repository name>
    tag: <a unique id that changes with every deploy>
    platform: linux/x86_64
    dockerfile: Dockerfile

schedule: null

push:
- prefect_docker.deployments.steps.push_docker_image:
    requires: prefect-docker>=0.3.1
    image_name: '{{ build_image.image_name }}'
    tag: '{{ build_image.tag }}'

pull:
  - prefect.deployments.steps.set_working_directory:
      directory: /opt/prefect/hello-world

deployments:
- name: modal-with-docker
  version: null
  tags: []
  description: null
  schedule: {}
  flow_name: null
  entrypoint: hello-world.py:my_flow
  parameters: {}
  work_pool:
    name: 'my-modal-pool'
    job_variables:
      image:
        tag: '{{ build_image.image_name }}:{{ build_image.tag }}'
        aws_secret: aws-secret
```

### Deploy and Run
Once these steps are complete and the above files created, you can do this:

```
prefect deploy
```

Prefect will ask you if you’d like to use an existing deployment configuration. Select `modal-with-docker` (it should be the only configuration available unless you’ve added others to the `prefect.yaml` file). Prefect will build your docker image, push it to ECR, create the deployment, and tell you how to view it in Prefect and run it.
So, run it:

```
prefect deployment run 'my-flow/modal-with-docker'
```

You can watch Prefect’s view of this by following the URL that Prefect gave you on the deploy step. You can watch Modal’s view of it on Modal’s `logs` page. You’ll see “Hello Modal!” displayed in Prefect’s view of the Run.

### Some Things to Look Out For
Make sure you’re authenticated to AWS, Modal and Prefect with your CLI tools.

Be sure to update the tag in your Docker image every time you deploy (I recommend automating this)

If Modal fails to fetch your image or execute it, it might give errors like:

````
19:45:53.933 | ERROR   | Flow run 'tan-camel' - [Errno 2] No such file or directory: '/opt/prefect/hello-world'
````

This can happen if your image can’t be retrieved from ECR. It’s deceptive because it looks like your Docker image is incorrectly formed. To check for this, see if the name of your Docker image appears in the Modal logs — if it doesn’t, there may be an error related to your AWS secrets.

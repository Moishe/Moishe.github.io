---
layout: post
title: itertools.product and dictionaries
description: A quick post about something fun in Python
---

As you know if you've talked to me for more than 5 seconds in the past 6 months, I've been working on [slime mold simulations](https://www.youtube.com/playlist?list=PLvaRSTa27UXl-43bB1wNAjRMkcyAOHwqD). One of my goals recently has been to specify all the behavior of a simulation in a config file, which will let me both re-create a given simulation, and will also let me script simulation behavior to tweak parameters in a systematic way.

So I have a config file that looks something like (lots of detail omitted):

```
base_config = {
    "colonies": {
        "dense": {
            "directionMomentum": 0.5,
            "directionRandomization": 0.4,
            "lookDistance": 5,
            "lookRadians": 1.0,
        }
    },
}
```

I initially wrote a script to mutate those fields inside a nested `for` loop, like so:

```
for radians in range(0,3):
    for dist in range(2,5):
        config['colonies']['dense']['lookRadians'] = 0.8 + radians / 4
        config['colonies']['dense']['lookDistance'] = dist
```

I could add more `for` loops if I wanted to change different variables, remove them if I didn't want 'em, etc. But this felt CLUNKY AND GROSS.

I am extraordinarily lucky to have a large number of friends who are both very knowledgable and willing to offer advice at the drop of a hat. I described this problem to some of them and learned about [`itertools.product`](https://docs.python.org/3/library/itertools.html#itertools.product), which effectively creates all the combinations of values that I was creating with my `for` loops above.

I needed a list of iterables to use `itertools.product`. I didn't exactly have that, but I realized I could specify iterables inside my struct, like so:

```
base_config = {
    "colonies": {
        "dense": {
            "directionMomentum": 0.1,
            "directionRandomization": 0.4,
            "lookDistance": range(2,5),
            "lookRadians": (0.8 + x / 4 for x in range(0, 3)),
        }
    },
}
```

Once I specified this, I could recursively create a list of iterables within the dictionary:

```
def find_iterables(d, p=[]):
    iterables = []
    for k,v in d.items():
        subp = p + [k]
        if type(v) == range or type(v) == types.GeneratorType:
            iterables.append((v, subp))
            d[k] = None # allow a deepcopy
        elif type(v) == dict:
            iterables += find_iterables(v, subp)

    return iterables
```

Couple of things to note here: first, notice that I'm not just checking for `range` types; I'm also checking for `generator` types. This lets me specify non-linear and non-integer ranges. Second, when I find one of these types, I overwrite its value in the descriptor dictionary to `None`. I do this because I need to make a deepcopy of the dictionary to populate it, and deepcopy won't work with these types.

Okay, so this method will return a list of iterables within the descriptor dictionary, and the path to them. Like this:

```
[
    (
        <generator object <genexpr> at 0x100ac6b30>,
        ['colonies', 'dense', 'lookRadians']
    ),
    (
        range(2, 5),
        ['colonies', 'dense', 'lookDistance']
    )
]
```

Now I can create a list of iterables to pass to `itertools.product`. I got to learn one more thing along the way, though: `itertools.product` is called like this:

```
results = itertools.product(range(0,3), range(0,3), (x / 10 for x in range(0,3)))
```

That is, you can pass an arbitrary number of parameters. This is accomplished with the `*` operator; all those args are packed into a tuple that the function can expand. But I have a list, and I want to expand that to a number of args. To do that, you can call the function like this (using the params from above)

```
iterables = [range(0,3), range(0,3), (x / 10 for x in range(0,3))]
results = itertools.product(*iterables)
```

The `*` expands the list into parameters. I'd never used this before and it was a delight to discover it!

With that knowledge I can implement the function to create all the instances of the structure:

```
def expand_dictionary(d):
    iterables = find_iterables(d)
    values = itertools.product(*[r[0] for r in iterables])
    for v in values:
        dc = copy.deepcopy(d)
        for (i, el) in enumerate(v):
            subd = dc
            for k in iterables[i][1][:-1]:
                subd = subd[k]
            subd[iterables[i][1][-1]] = el
        yield dc
```

With the initial specification above, this emits 9 specific configurations; the first two look like this:

```
  {
    "colonies": {
      "dense": {
        "directionMomentum": 0.1,
        "directionRandomization": 0.4,
        "lookDistance": 0,
        "lookRadians": 0.8
      }
    }
  },
  {
    "colonies": {
      "dense": {
        "directionMomentum": 0.1,
        "directionRandomization": 0.4,
        "lookDistance": 0,
        "lookRadians": 1.05
      }
    }
  }
```

Using the complete configurations, I can run my simulation and get an output like this:

![A 9-grid of different images of a tree](/images/radians_by_distance.jpg)

Magic!

Here's a [link to my implementation](https://github.com/Moishe/metal-mold-2/blob/main/batch-runner/dict_product.py)
# Jekyll container from Ruby Alpine image optimized for ARM (M1 Mac)
FROM ruby:2.7-alpine

# Add Jekyll dependencies to Alpine
RUN apk update && apk add --no-cache \
    build-base \
    gcc \
    cmake \
    git \
    nodejs \
    npm \
    zlib-dev \
    libffi-dev

# Working directory for the app
WORKDIR /site

# Copy Gemfile for dependency installation
COPY Gemfile Gemfile.lock* ./

# Install bundler and dependencies (specify bundler version for Ruby 2.7)
RUN gem install bundler -v 2.4.22
RUN bundle install

# Copy the rest of the site
COPY . .

# Fix permission issues that might occur with mounted volumes
RUN chmod -R 777 /site

# Expose port 4000 for Jekyll server
EXPOSE 4000

# Command to run when the container starts
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
#!/bin/bash

# ABOUTME: Script to run Jekyll site locally using Docker
# ABOUTME: Builds Docker image and serves site on localhost:4000

set -e

echo "🚀 Starting Jekyll site with Docker..."

# Build the Docker image
echo "📦 Building Docker image..."
docker build -t jekyll-site .

# Run the container with port mapping and volume mount
echo "🌐 Starting Jekyll server on http://localhost:4000"
echo "💡 Press Ctrl+C to stop the server"
echo ""

docker run --rm -p 4000:4000 -v $(pwd):/site jekyll-site
#!/bin/bash

# Exit on error
set -e

IMAGE_NAME="mayfieldguitars-test"
PORT=${PORT:-8000}

echo "Building Docker image..."
sudo docker build --build-arg PORT=$PORT -t $IMAGE_NAME .

echo "Running Docker container in detached mode..."
CONTAINER_ID=$(sudo docker run -d -p $PORT:$PORT -e PORT=$PORT $IMAGE_NAME)

# Give the server a moment to start
sleep 5

echo "Checking if the website is running..."
if ! curl -s --fail http://localhost:$PORT | grep -q "guitar prototype at mayfield ave"; then
    echo "Test failed: Website is not running correctly."
    sudo docker logs $CONTAINER_ID
    sudo docker stop $CONTAINER_ID
    exit 1
fi

echo "Test passed: Website is running correctly."
echo "Stopping the container..."
sudo docker stop $CONTAINER_ID
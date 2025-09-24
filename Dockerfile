# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install Nikola
RUN pip install "Nikola[extras]"

# Copy the website content into the container
COPY mayfieldguitars.com/ .

# Build the website
RUN nikola build

# Expose port 8000 and start a simple HTTP server
ENV PORT 8000
EXPOSE $PORT
CMD python -m http.server $PORT --directory output
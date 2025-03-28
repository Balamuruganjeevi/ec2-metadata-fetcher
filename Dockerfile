# Use Alpine Linux as the base image
FROM alpine:latest

# Install dependencies: Python and curl
RUN apk add --no-cache python3 py3-pip curl

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY ec2_metadata_fetcher.py .

# Set execution permissions
RUN chmod +x ec2_metadata_fetcher.py

# Set the default command
ENTRYPOINT ["python3", "/app/ec2_metadata_fetcher.py"]


# ec2-metadata-fetcher
DevOps Technical Assessment – AWS EC2 Instance Metadata Fetcher

Steps to create and install 
Prerequisites

✅ Docker
✅ Python 3
✅ Bash Shell
✅ AWS CLI
✅ LocalStack
✅ Minikube
✅ Helm

Step 1: Set Up LocalStack
Step 2: Create the Python Script
  Create a file fetch_metadata.py
  Run the script:
  python fetch_metadata.py IMDSv2
Step 3: Create Dockerfile
  Create a Dockerfile:
Step 4: Build and Push Docker Image
Build the Docker image:
  docker build -t <your-dockerhub-username>/ec2-metadata-fetcher .
Log in to Docker Hub:
  docker login
Push the image:
  docker push <your-dockerhub-username>/ec2-metadata-fetcher
Test the image:
  docker run --rm <your-dockerhub-username>/ec2-metadata-fetcher IMDSv2
Step 5: Create Helm Chart
  helm create ec2-metadata-chart
  Update values.yaml
  Update templates/deployment.yaml
Step 6: Install the Helm Chart
Package the chart:
  helm package .
Install it on Minikube:
  helm install ec2-fetcher ./ec2-metadata-fetcher
Verify deployment:
  kubectl get pods
Access the pod manually:
  kubectl exec -it <pod-name> -- /bin/sh


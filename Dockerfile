FROM alpine:latest
RUN apk add --no-cache python3 py3-pip
COPY ec2_metadata_fetcher.py /app/
WORKDIR /app
ENTRYPOINT ["python3", "ec2_metadata_fetcher.py"]


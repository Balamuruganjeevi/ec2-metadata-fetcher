import argparse
import json
import subprocess

# EC2 Metadata Base URL
IMDS_BASE_URL = "http://169.254.169.254/latest/meta-data/"

def fetch_metadata(imds_version):
    metadata = {}

    try:
        if imds_version == "v2":
            # Get Token for IMDSv2
            token_cmd = [
                "curl", "-s", "-X", "PUT",
                IMDS_BASE_URL + "../api/token",
                "-H", "X-aws-ec2-metadata-token-ttl-seconds: 21600"
            ]
            token = subprocess.check_output(token_cmd, text=True).strip()
            headers = ["-H", f"X-aws-ec2-metadata-token: {token}"]
        else:
            # No token required for IMDSv1
            headers = []

        # Fetch instance metadata
        for key in ["instance-id", "instance-type", "placement/availability-zone"]:
            cmd = ["curl", "-s"] + headers + [IMDS_BASE_URL + key]
            metadata[key.split("/")[-1]] = subprocess.check_output(cmd, text=True).strip()

    except subprocess.CalledProcessError as e:
        print(json.dumps({"error": f"Failed to fetch metadata: {str(e)}"}))
        return

    # Print JSON output
    print(json.dumps(metadata, indent=4))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch EC2 Instance Metadata")
    parser.add_argument(
        "--imds-version", choices=["v1", "v2"], default="v2",
        help="Specify whether to use IMDSv1 or IMDSv2 (default: v2)"
    )
    
    args = parser.parse_args()
    fetch_metadata(args.imds_version)


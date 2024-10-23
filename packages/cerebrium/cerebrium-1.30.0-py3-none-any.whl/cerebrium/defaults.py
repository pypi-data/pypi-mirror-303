from sys import version_info

# Deployment
PYTHON_VERSION = f"{version_info.major}.{version_info.minor}"
DOCKER_BASE_IMAGE_URL = "debian:bookworm-slim"
INCLUDE = ["./*", "main.py", "cerebrium.toml"]
EXCLUDE = [".*"]
SHELL_COMMANDS = []

# Custom Runtime
ENTRYPOINT = ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
PORT = 8000
HEALTHCHECK_ENDPOINT = "/readyz"

# Hardware
CPU = 2
MEMORY = 12.0
COMPUTE = "CPU"
GPU_COUNT = 1
PROVIDER = "aws"
REGION = "us-east-1"

# Scaling
MIN_REPLICAS = 0
MAX_REPLICAS = 5
COOLDOWN = 30
REPLICA_CONCURRENCY = 1

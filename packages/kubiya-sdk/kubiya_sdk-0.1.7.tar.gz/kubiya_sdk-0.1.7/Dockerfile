# Use an official Python runtime as the base image
FROM python:3.11-slim-buster
COPY --from=ghcr.io/astral-sh/uv:0.4.22 /uv /uvx /bin/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    git \
    libpq-dev \
    python3-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY uv.lock .
COPY pyproject.toml .
RUN uv sync --frozen

# Add virtual environment to $PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy the SDK source code
COPY kubiya_sdk ./kubiya_sdk
COPY README.md .

# Install the SDK
RUN uv pip install --no-cache-dir -e .

# Create a symlink to the CLI script
RUN ln -s /app/kubiya_sdk/cli.py /usr/local/bin/cli.py

# Make the CLI script executable
RUN chmod +x /usr/local/bin/cli.py
RUN chmod +x /app/kubiya_sdk/cli.py

# Set the entrypoint to the CLI script
ENTRYPOINT ["python", "/usr/local/bin/cli.py"]

# Use CMD to provide default arguments to the entrypoint
CMD ["--help"]

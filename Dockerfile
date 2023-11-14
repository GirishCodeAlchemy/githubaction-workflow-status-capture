FROM python:3.10-slim

# Install git
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy scripts
COPY scripts /app/

# Set the entrypoint script as executable
RUN chmod +x /app/entrypoint.sh

# Define the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

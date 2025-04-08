# Use an official Python runtime as a parent image
FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean

# Install Ollama
RUN curl -sSL https://ollama.com/install.sh | bash

# Ensure ollama is installed
RUN which ollama

# Create a directory for the app
WORKDIR /app

# Copy your Python script (if you have one) to the container
COPY . /app

# Install Python dependencies if you have any (for example, Flask)
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port your app will run on
EXPOSE 5000

# Run the app (adjust with your script entry point)
CMD ["python3", "app.py"]

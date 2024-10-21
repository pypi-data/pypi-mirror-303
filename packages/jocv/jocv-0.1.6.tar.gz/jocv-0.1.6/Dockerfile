# Use the official Rust image as a parent image
FROM rust:latest

# Update the system and install pip and python3.11-venv
RUN apt-get update && apt-get install -y python3-pip python3.11-venv

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Add the venv bin directory to PATH
ENV PATH="/opt/venv/bin:$PATH"

# Install maturin
RUN pip install maturin numpy
# Use the PyTorch base image with CUDA support
FROM pytorch/pytorch:2.1.1-cuda12.1-cudnn8-runtime

# Copy the contents of the local 'app' directory to the '/app' directory in the Docker image
COPY ./app /app

# Install dependencies specified in 'requirements.txt'
RUN pip install -r /app/requirements.txt

# Set the working directory for subsequent instructions
WORKDIR /app
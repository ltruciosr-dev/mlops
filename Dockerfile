FROM pytorch/pytorch:2.1.1-cuda12.1-cudnn8-runtime

# Install any dependencies
COPY ./app /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Set the working directory
WORKDIR /app
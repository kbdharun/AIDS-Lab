# Use the latest Ubuntu image as the base image
FROM ubuntu:latest

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y

# Install python, pip, git, and Jupyter Notebook
RUN apt-get install -y python3 python3-pip git
RUN pip3 install notebook

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install Python packages from requirements file
RUN pip3 install -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Command to run when the container starts
CMD ["/bin/bash"]

# Use the latest Ubuntu image as the base image
FROM ubuntu:latest

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y

# Install python, pip, git, and Jupyter Notebook
RUN apt-get install -y python3 python3-pip git
RUN pip3 install notebook

# Install python packages
RUN pip3 install matplotlib 
RUN pip3 install networkx 
RUN pip3 install scipy

# Set the working directory
WORKDIR /app

# Command to run when the container starts
CMD ["/bin/bash"]

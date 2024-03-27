# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:22.04




# Install pip requirements
RUN apt-get update && \
      apt-get -y install sudo
RUN sudo apt update
RUN sudo apt install -y python3
RUN sudo apt install -y python3-pip
RUN sudo apt install -y mysql-server
RUN sudo apt install -y mysql-client
RUN sudo pip3 install mysql-connector-python

WORKDIR /app
COPY . /app
# RUN chmod +x entrypoint.sh 
RUN chmod +x installation.sh 
#RUN ./installation.sh
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# ENTRYPOINT [ "entrypoint.sh" ]

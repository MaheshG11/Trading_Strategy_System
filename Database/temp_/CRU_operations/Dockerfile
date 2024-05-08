# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3




# Install pip requirements
#RUN install -y python3-pip
RUN pip3 install mysql-connector-python

WORKDIR /app
COPY . /app
# RUN chmod +x entrypoint.sh 
#RUN ./installation.sh
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# ENTRYPOINT [ "entrypoint.sh" ]

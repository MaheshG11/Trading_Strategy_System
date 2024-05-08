# For more information, please refer to https://aka.ms/vscode-docker-python
FROM mysql


COPY Database_layout.sql /docker-entrypoint-initdb.d
# RUN chmod +x entrypoint.sh 
#RUN ./installation.sh
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# ENTRYPOINT [ "entrypoint.sh" ]

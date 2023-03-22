ARG PYTHON_VER

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:${PYTHON_VER}-slim

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# set the working directory in the container
WORKDIR /app

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# copy the content of the local src directory to the working directory
# this isn't needed when developing as there's a bind under volumes: in the docker-compose.dev.yml file
COPY src .

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:5000", "app:app"]

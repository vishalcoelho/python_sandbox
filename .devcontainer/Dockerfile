# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/codespaces-linux/.devcontainer/base.Dockerfile
FROM mcr.microsoft.com/vscode/devcontainers/universal:2-focal


RUN apt-get update && apt-get -y install --no-install-recommends \
  python3.8-venv
  
  
ARG USERNAME=codespace
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG HOMEDIR=/home/$USERNAME
ARG VENV_PATH=$HOMEDIR/venv

COPY requirements.txt /tmp/
COPY Makefile /tmp/

RUN su $USERNAME -c "/usr/bin/python3 -m venv $VENV_PATH" \
  && su $USERNAME -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt" \
  && rm -rf /tmp/requirements.txt

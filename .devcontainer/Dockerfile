# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/codespaces-linux/.devcontainer/base.Dockerfile
FROM mcr.microsoft.com/vscode/devcontainers/universal:2-focal


RUN apt install software-properties-common -y \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get update \
    && apt-get -y install --no-install-recommends \
        python3.8-venv


ARG USERNAME="codespace"
ARG VENV_PATH="/home/${USERNAME}/venv"

COPY requirements.txt /tmp/
COPY Makefile /tmp/

RUN su $USERNAME -c "/usr/bin/python3 -m venv ${VENV_PATH}" \
  && su $USERNAME -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt" \
  && rm -rf /tmp/requirements.txt

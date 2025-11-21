
FROM rockylinux:9.3 AS base

ARG REPO_NAME=py-play
ARG USERNAME=guido
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN set -eux -o pipefail && \
    dnf install --setopt=***.sslverify=false -y dnf-utils dnf-plugins-core epel-release
RUN set -eux -o pipefail && \
    dnf install --setopt=***.sslverify=false -y ca-certificates curl-minimal git jq sudo which rsync
RUN set -eux -o pipefail && \
    dnf install --setopt=***.sslverify=false -y python3 python3-pip

RUN set -eux -o pipefail && \
    pip install flask && \
    curl -kLsSf https://astral.sh/uv/install.sh | sh

# envs
ENV INSTALL_PATH="/usr/local"
ENV PATH="${HOME}/bin:${PATH}"

# Create the user
RUN groupadd --gid ${USER_GID} ${USERNAME} && \
  useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} -s /bin/zsh && \
  echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} && \
  chmod 0440 /etc/sudoers.d/${USERNAME}

########### NON ROOT FROM HERE DOWN ###########
FROM base AS user

USER ${USERNAME}

RUN set -eux && \
    sudo mkdir -p /workdir/${REPO_NAME} && \
    sudo chown ${USERNAME}:${USERNAME} /workdir

# envs
ENV HOME="/home/${USERNAME}"
ENV SDK_HOME=${HOME}/sdk
ENV PATH=${HOME}/bin:${PATH}

# pretty bash
COPY --chown=${USERNAME}:${USERNAME} .bash_pretty ${HOME}/.bash_pretty
RUN set -eux && \
    echo "source ${HOME}/.bash_pretty" >> ${HOME}/.bashrc

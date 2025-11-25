FROM rockylinux:9 AS base

ARG REPO_NAME=py-play
ARG USERNAME=guido
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Add ca certs so we can build the image on vpn
COPY cas.pem /etc/pki/ca-trust/source/anchors/custom_cas.pem 
RUN update-ca-trust

RUN set -eux -o pipefail && \
    dnf --setopt=***.sslverify=false install -y epel-release && \
    dnf --setopt=***.sslverify=false -y update
RUN set -eux -o pipefail && \
    dnf --setopt=***.sslverify=false install -y ca-certificates curl-minimal git jq lsof python3 python3-pip sudo which rsync zsh

# envs
ENV PATH="${HOME}/bin:${PATH}"

# Create the user
RUN groupadd --gid ${USER_GID} ${USERNAME} && \
  useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} -s /bin/bash && \
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
ENV PATH=${HOME}/bin:${HOME}/.local/bin:${PATH}

# pretty bash
COPY --chown=${USERNAME}:${USERNAME} .bash_pretty ${HOME}/.bash_pretty
RUN set -eux && \
    echo "source ${HOME}/.bash_pretty" >> ${HOME}/.bashrc

# assume no validation so we can work on corp networks w/o requiring CAs
RUN set -eux && \
    echo "alias dnf='dnf --setopt=***.sslverify=false'" >> ${HOME}/.bashrc

RUN set -eux && \
    curl -kLsSf https://astral.sh/uv/install.sh | sh && \
    uv install python3.14 && \
    uv python pin 3.14 && \
    python3.14 -m venv .venv && \
    uv add flask google-adk google-genai && \
    source .venv/bin/activate || true

ENV GOOGLE_API_KEY="TODO: SET THIS"

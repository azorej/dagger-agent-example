FROM ubuntu:jammy

SHELL ["/bin/bash", "-o", "pipefail", "-o", "errexit", "-o", "nounset", "-o", "xtrace", "-c"]

USER root

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC \
    DAGGER_VERSION=0.18.7

RUN apt-get update -y && apt-get install -y \
    curl \
    wget \
    jq \
    git \
    apt-transport-https \
    gnupg \
    python3 \
    python3-pip \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    python3-venv \
    build-essential \
    libdbus-1-dev libdbus-glib-1-dev \
    sudo \
    locales \
    tzdata \
    zsh \
    # https://github.com/BurntSushi/ripgrep
    ripgrep \
    # https://github.com/sharkdp/bat
    bat \
    && rm -rf /var/lib/apt/lists/*

# Install Github cli: https://github.com/cli/cli/blob/trunk/docs/install_linux.md
RUN mkdir -p -m 755 /etc/apt/keyrings \
        && out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        && cat $out | tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& apt update \
	&& apt install gh -y \
    && rm -rf /var/lib/apt/lists/*

# Install Dagger: https://docs.dagger.io/install/
RUN curl -fsSL https://dl.dagger.io/dagger/install.sh | BIN_DIR=/usr/bin sh

RUN pip install pre-commit ruff

# Set locale
RUN locale-gen en_US.UTF-8

# Add terminal colors
RUN echo "PS1='\e[92m\u\e[0m@\e[94m\h\e[0m:\e[35m\w\e[0m# '" >> /root/.bashrc

# Setup non-root user
ARG USER
ARG USER_UID=1000
ARG USER_GID=$USER_UID

COPY setup_user.sh setup_terminal.sh .zshrc /devcontainer_bootstrap/
RUN /devcontainer_bootstrap/setup_user.sh

USER $USER

RUN /devcontainer_bootstrap/setup_terminal.sh

# Install uv: https://github.com/astral-sh/uv?tab=readme-ov-file#installation
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
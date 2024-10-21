FROM python:3.12-slim-bookworm

# Setup uv.
COPY --from=ghcr.io/astral-sh/uv:0.4.20 /uv /bin/uv

# Need bash-completion for bash completion, curl to download startship.rs, and ssh for Git.
RUN apt-get update && apt-get install -y bash-completion build-essential curl ssh

# Setup bash completion
RUN echo "source /etc/bash_completion" >> ~/.bashrc

# Setup starship prompt
RUN curl -sS https://starship.rs/install.sh | sh -s -- -y
RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc

# Set VS Code as default editor
RUN echo 'export EDITOR="code "' >> ~/.bashrc

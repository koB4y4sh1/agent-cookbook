FROM python:3.11-slim AS base

## システム依存ライブラリ
RUN apt-get update && apt-get install -y \
    curl git bash build-essential \
    && rm -rf /var/lib/apt/lists/*

# ユーザー作成 (vscodeユーザー)
RUN useradd -m vscode && \
echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# 最新pipとuv
RUN pip install --upgrade pip uv

WORKDIR /workspace

# pyproject.toml を先にコピー（Dockerキャッシュのため）
COPY pyproject.toml .

# コピーしつつ所有者をvscode ユーザーに指定することで権限付与
COPY --chown=vscode:vscode . .

USER vscode
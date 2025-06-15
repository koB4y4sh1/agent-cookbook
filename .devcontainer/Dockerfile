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

# パッケージのインストール（必要ならここで入れてもよい）
RUN uv sync

COPY . .

# 権限を vscode ユーザーに変更
RUN chown -R vscode:vscode /workspace

USER vscode
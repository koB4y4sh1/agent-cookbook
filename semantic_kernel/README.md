# Semantic Kernel 入門ハンズオン

このディレクトリでは、Microsoft Semantic Kernel（SK）を使ったプラグインベースのエージェント開発を学びます。

## 🔧 前提

- Python 3.10+
- `uv` による依存管理
- `.env` に APIキーなどを記載

```bash
uv venv
source .venv/bin/activate
uv pip install --requirements requirements.txt
```

## 📚 内容一覧

| ファイル               | 内容                       |
| ------------------ | ------------------------ |
| `00_hello_sk.py`   | LLM呼び出しの最小例              |
| `01_plugins.py`    | プラグインの定義と実行方法            |
| `02_chaining.py`   | スキルチェーンの作成               |
| `03_memory.py`     | メモリ（Semantic Memory）の導入例 |
| `04_agent_loop.py` | Agentループによる問題解決タスク       |

## 📘 使用ライブラリ

- [semantic-kernel](https://github.com/microsoft/semantic-kernel)
- openai, python-dotenv など

## 📝 .env 例
```env
OPENAI_API_KEY=sk-xxxxxx
```

## 📌 備考
Semantic Kernel は C# にも対応しているため、将来的にはマルチランタイムの検証も可能です。
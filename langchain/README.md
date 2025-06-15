# LangChain 入門ハンズオン

このディレクトリでは、LangChain を用いたエージェント開発の基本を学びます。

## 📦 前提環境

- Python 3.10+
- `uv` によるパッケージ管理
- `.env` に OpenAI APIキーなどを記載

```bash
uv venv
source .venv/bin/activate
uv pip install --requirements requirements.txt
```
## 🔧 主要ライブラリ

- LangChain
- OpenAI
- python-dotenv（環境変数読み込み）

## 📚 内容

| ファイル                     | 説明                   |
| ------------------------ | -------------------- |
| `00_hello_langchain.py`  | LLM応答の最小コード          |
| `01_prompt_template.py`  | PromptTemplateの使い方   |
| `02_chains.py`           | LLMChainなどの基本Chain   |
| `03_tools_and_agents.py` | ツールとAgentの導入例        |
| `04_memory.py`           | 会話履歴の保持（Memory）機能    |
| `05_langgraph_intro.py`  | LangGraphの導入（必要に応じて） |

## 📝 .env 例
```env
OPENAI_API_KEY=sk-xxxxxx
```

## 🔜 今後の拡張案

- LangGraph を使ったプロセスベースのAgent設計
- Supabaseや外部データとの統合


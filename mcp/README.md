# Multi-Agent Control Plane（MCP）ハンズオン

このディレクトリでは、LangChain MCP（Multi-agent Control Plane）を用いて、複数エージェントの制御と協調を実現する手法を学びます。

## 🧠 MCPとは？

> LangChain MCP は、複数のツール・エージェント・LLMタスクをプロセス化して制御する仕組みです。

## 🛠 セットアップ

```bash
uv venv
source .venv/bin/activate
uv pip install --requirements requirements.txt
```

## 📚 内容一覧

| ファイル/ディレクトリ                      | 説明                  |
| -------------------------------- | ------------------- |
| `00_intro_mcp.py`                | MCPの基本概念と最小例        |
| `01_multi_agent_coordination.py` | 2つ以上のエージェントの連携      |
| `02_mcp_with_langgraph.py`       | LangGraphと統合したMCP構成 |
| `03_task_delegation.py`          | タスク分割と委任処理の例        |

## 📝 .env 例

```env
OPENAI_API_KEY=sk-xxxxxx
```

## 📌 今後の展望

- LangGraph上でMCPノードを組み合わせた複雑フローの構築
- UI（Gradio）などとの統合による対話型システム化


---

## ✅ 各フォルダに共通する運用ルール（補足）

- 各サブディレクトリに `.env.example` を配置
- `requirements.txt` または `pyproject.toml` を個別に配置
- `.ipynb` ファイルと `.py` ファイルの両対応が可能

---
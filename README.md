# AI Agent Cookbook

LLMベースのエージェント技術（LangChain / Semantic Kernel / MCP）を段階的に学習・比較するためのハンズオン集です。

## 🔍 構成と学習順序

1. **LangChain入門**
   - [00_hello_agent.py](./langchain/00_hello_agent.py): 最小構成のAgent
   - [01_tool_use_agent.py](./langchain/01_tool_use_agent.py): 外部ツール統合
   - [02_react_agent.ipynb](./langchain/02_react_agent.ipynb): ReActパターン
   - [03_multi_agent_messaging.py](./langchain/03_multi_agent_messaging.py): LangGraphによるマルチAgent

2. **Semantic Kernel入門**
   - [00_basic_kernel_init.ipynb](./semantic_kernel/00_basic_kernel_init.ipynb)
   - [01_planner_skills_chat.ipynb](./semantic_kernel/01_planner_skills_chat.ipynb)
   - [02_function_calling_tools.py](./semantic_kernel/02_function_calling_tools.py)

3. **MCP（Multi-agent Control Plane）実験**
   - [00_overview.md](./mcp/00_overview.md): MCPの全体像
   - [02_mcp_agent_executor.py](./mcp/02_mcp_agent_executor.py): 簡易MCP実装（LangGraphベース）

4. **Playground（応用・比較・実験）**
   - LangGraphフロー設計例
   - 複数モデルの比較評価
   - 自作ツール・メモリのテスト

## 🛠️ セットアップ手順（推奨: Dev Container）
``` powershell
# uvのインストール　https://docs.astral.sh/uv/getting-started/installation/
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.7.13/install.ps1 | iex"
```

```bash
# 初回セットアップ
git clone https://github.com/your-org/ai-agent-cookbook.git
cd ai-agent-cookbook
cp .env.example .env
uv venv
. .venv/scripts/activate
uv sync
```
# エージェントアーキテクチャの全体像

## エージェント技術のレイヤー構造
[LLM API]
│
├─ LangChain
│ ├─ Agent Executor
│ ├─ Tool Integration
│ └─ LangGraph（マルチAgent構成）
│
├─ Semantic Kernel
│ ├─ Kernel + Planner
│ ├─ Skill / Function呼び出し
│ └─ Context Memory
│
└─ MCP
  ├─ Task Dispatcher
  ├─ Agent Orchestrator
  └─ Memory Store / Router

## 推奨学習順

1. 単一Agentの基本理解（LangChain）
2. ツールやメモリの統合
3. マルチエージェント連携（LangGraph）
4. Semantic Kernelとの比較
5. MCPによる複雑な制御・再利用性の高い構成の設計

# Playground：AIエージェント開発の実験場

このディレクトリは、LangChain / Semantic Kernel / MCP などのライブラリを自由に組み合わせて試すための「プレイグラウンド」です。

## 🎯 目的

- 概念検証（PoC）や試作コードの作成
- 機能比較やライブラリ同士の統合テスト
- 実験コードの一時的な置き場として活用

## 🛠 環境セットアップ

```bash
uv venv
source .venv/bin/activate
uv pip install --requirements requirements.txt
```
または、pyproject.toml がある場合：

```bash
uv pip install -r requirements.txt
```

## 🧪 サンプル実験一覧
| ファイル名                         | 説明                                    |
| ----------------------------- | ------------------------------------- |
| `01_langchain_vs_sk.py`       | LangChainとSemantic Kernelで同一タスクを実装し比較 |
| `02_agent_loop_test.py`       | 明示的なループ処理による自律エージェントの試作               |
| `03_tool_integration_test.py` | 複数ツール（検索、計算、翻訳など）の統合検証                |
| `04_langgraph_custom_node.py` | LangGraphに独自ノードを追加するサンプル              |
| `scratchpad.ipynb`            | Jupyter Notebookでの実験用ノート              |

## 📌 注意事項
このディレクトリ内のコードは安定動作を保証しません。あくまで実験・試験的な目的で使用してください。
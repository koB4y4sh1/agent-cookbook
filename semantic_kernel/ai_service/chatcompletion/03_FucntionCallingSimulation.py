# 03_FucntionCallingSimulation.py

import asyncio
from dotenv import load_dotenv

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.contents.function_call_content import FunctionCallContent
from semantic_kernel.contents.function_result_content import FunctionResultContent
from semantic_kernel.contents.utils.author_role import AuthorRole

load_dotenv()

async def main():

    # 環境変数からの設定読み取り
    chat_completion_service = AzureChatCompletion(service_id="my-service-id")
    
    # プロンプトオブジェクト作成
    execution_settings = OpenAIChatPromptExecutionSettings()

    # ChatHistoryオブジェクト作成
    chat_history = ChatHistory()

    # FunctionCallingを疑似的に再現
    chat_history.add_user_message("ユーザーID`test0001user`,`test9999user`に対応する名前を教えてください。")
    chat_history.add_message(
        message=ChatMessageContent(
            role=AuthorRole.ASSISTANT,
            items=[
                FunctionCallContent(
                    name="get_user_name",
                    id="0001",
                    arguments=str({"userid":"test0001user"})
                ),
                FunctionCallContent(
                    name="get_user_name",
                    id="0002",
                    arguments=str({"userid":"test9999user"})
                )
            ]
        )
    )
    
    # 関数の実行を疑似的に再現
    chat_history.add_message(
        message=ChatMessageContent(
            role=AuthorRole.TOOL,
            items=[
                FunctionResultContent(
                    name="get_user_name",
                    id="0001",
                    result="{\"username\":\"FukuharaMomo\"}",
                )
            ]
        )
    )
    chat_history.add_message(
        message=ChatMessageContent(
            role=AuthorRole.TOOL,
            items=[
                FunctionResultContent(
                    name="get_user_name",
                    id="0002",
                    result="{\"username\":\"KobayashiKento\"}",
                )
            ]
        )
    )

    response = await chat_completion_service.get_chat_message_content(
        chat_history=chat_history,
        settings=execution_settings,
    )
    print(response)
    
if __name__ == "__main__":
    asyncio.run(main())

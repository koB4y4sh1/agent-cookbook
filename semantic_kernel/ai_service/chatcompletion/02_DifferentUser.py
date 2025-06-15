# 02_DifferentUser.py

import asyncio
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.contents.text_content import TextContent
from semantic_kernel.contents.image_content import ImageContent
from semantic_kernel.contents.utils.author_role import AuthorRole

load_dotenv()

async def main():

    # 環境変数からの設定読み取り
    chat_completion_service = AzureChatCompletion(service_id="my-service-id")
    
    # プロンプトオブジェクト作成
    execution_settings = OpenAIChatPromptExecutionSettings()

    # ChatHistoryオブジェクト作成
    chat_history = ChatHistory()

    # 多様な追加方法
    chat_history.add_message(
        message=ChatMessageContent(
            role=AuthorRole.SYSTEM,
            content="赤ちゃん言葉で話してください。また、文の最初は`こんにちは<名前>!`で始めてください"
        )
    )
    
    # 画像含むメッセージ
    chat_history.add_message(
        message=ChatMessageContent(
            role=AuthorRole.USER,
            name="JhoneDante",
            items=[
                TextContent(text="こんにちは！私の名前はジョンです。"),
                ImageContent(uri="https://stgptappdev001.blob.core.windows.net/sample/sample.jpg"),
            ]
        )
    )
    
    # AIメッセージ
    chat_history.add_message(
        message=ChatMessageContent(
            role=AuthorRole.ASSISTANT,
            name="AssistantForJhone",
            content="こんにちは、ジョンさん！はじめまして。今日はどのようにお手伝いできますか？"
        )
    )
    
    # 別のユーザーのメッセージを追加する
    chat_history.add_message(
        message=ChatMessageContent(
            role=AuthorRole.ASSISTANT,
            name="EmaWatson",
            content="こんにちは！私の名前は分かる？"
        )
    )

    response = await chat_completion_service.get_chat_message_content(
        chat_history=chat_history,
        settings=execution_settings,
    )
    print(response)
    
if __name__ == "__main__":
    asyncio.run(main())

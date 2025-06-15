# 05_MultiMordalChat.py

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
    chat_completion_service =AzureChatCompletion()

    # ChatHistoryオブジェクト作成
    chat_history = ChatHistory()
    chat_history.add_system_message("あなたの仕事は画像について説明することです。")
    
    # 画像含むメッセージ（URL）
    chat_history.add_message(
        message=ChatMessageContent(
            role=AuthorRole.USER,
            name="JhoneDante",
            items=[
                TextContent(text="この写真には何が写っているでしょうか？"),
                ImageContent(uri="https://stgptappdev001.blob.core.windows.net/sample/sample.jpg"),
            ]
        )
    )

    
    # 画像含むメッセージ（ローカルファイル）
    chat_history.add_message(
        message=ChatMessageContent(
            role=AuthorRole.USER,
            name="JhoneDante",
            items=[
                TextContent(text="この写真には何が写っているでしょうか？"),
                ImageContent.from_image_file(path="data/cat.jpg"),
            ]
        )
    )

    response = await chat_completion_service.get_chat_message_content(chat_history,OpenAIChatPromptExecutionSettings())
    print(response)

if __name__ == "__main__":
    asyncio.run(main())

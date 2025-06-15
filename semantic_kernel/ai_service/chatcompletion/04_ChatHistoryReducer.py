# 04_ChatHistoryReducer.py

import asyncio
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistoryTruncationReducer
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.contents.text_content import TextContent
from semantic_kernel.contents.image_content import ImageContent
from semantic_kernel.contents.utils.author_role import AuthorRole

load_dotenv()

async def main():
    kernel = Kernel()
    kernel.add_service(AzureChatCompletion())
    
    # 最新の２つのメッセージを保持する
    truncation_reducer = ChatHistoryTruncationReducer(
        target_count=2
    )
    truncation_reducer.add_system_message("You are a helpful assistant.")

    is_reduced = False

    while True:
        user_input = input("User:> ")
        if user_input.lower() == "exit":
            print("\n\nExiting chat ...")
            break

        is_reduced = await truncation_reducer.reduce()
        if is_reduced:
            print(f"@メッセージの履歴{len(truncation_reducer.messages)}件に削減しました。")
        
        response = await kernel.invoke_prompt(
            prompt="{{$chat_history}}{{$user_input}}",user_input=user_input, chat_history=truncation_reducer
        )

        if response:
            print(f"Assistant:> {response}")
            truncation_reducer.add_user_message(str(user_input))
            truncation_reducer.add_message(response.value[0])
    
    if is_reduced:
        for msg in truncation_reducer.messages:
            print(f"{msg.role} - {msg.content}\n")
        print("\n")
    
if __name__ == "__main__":
    asyncio.run(main())

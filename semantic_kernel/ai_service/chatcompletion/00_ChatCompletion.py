# 00_ChatCompletion.py

import asyncio
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings
from semantic_kernel.contents.chat_history import ChatHistory

load_dotenv()

async def main():
    # カーネルを初期化します
    kernel = Kernel()
    
    # 例：ChatCompletion APIを使用する
    # chat_completion_service = AzureChatCompletion(
    #     deployment_name="my-deployment",  
    #     api_key="my-api-key",
    #     endpoint="my-api-endpoint", 
    #     service_id="my-service-id",
    # )

    # 例：環境変数からの設定読み取り
    # ID指定によりSemantic Kernel内の特定のサービスをタグ付けできる
    chat_completion_service = AzureChatCompletion(service_id="my-service-id")
    
    # プロンプトオブジェクト作成
    execution_settings = OpenAIChatPromptExecutionSettings()

    # ChatHistoryオブジェクト作成
    chat_history = ChatHistory()
    chat_history.add_user_message("こんにちは！私の名前はジョンです。")

    
    # 上で作成したチャット補完サービスをカーネルに追加します
    kernel.add_service(chat_completion_service)

    # サービスIDでカーネルに登録したサービスを取得できる
    chat_completion_service:AzureChatCompletion = kernel.get_service(service_id="my-service-id")

    
    response = await chat_completion_service.get_chat_message_content(
        chat_history=chat_history,
        settings=execution_settings,
    )
    print(response)
    
if __name__ == "__main__":
    asyncio.run(main())

import httpx
from config import settings
from logger import logger

async def get_augmented_response(chatbot_reply: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            settings.LLM_API_URL,
            json={"text": chatbot_reply},
            timeout=10.0
        )
    if response.status_code == 200:
        data = response.json()
        return data.get("augmented_text", chatbot_reply)
    else:
        logger.error(f"LLM API error: {response.text}")
        return chatbot_reply
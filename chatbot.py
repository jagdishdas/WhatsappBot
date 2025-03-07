import httpx
from config import settings
from logger import logger

async def get_chatbot_response(incoming_message: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            settings.CHATBOT_API_URL,
            json={"query": incoming_message},
            timeout=10.0
        )
    if response.status_code == 200:
        data = response.json()
        return data.get("response", "I didn't understand that.")
    else:
        logger.error(f"Chatbot API error: {response.text}")
        return "Sorry, I couldn't process your message."
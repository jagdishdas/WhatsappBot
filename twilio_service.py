from twilio.rest import Client
from config import settings
from logger import logger

twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to: str, body: str):
    try:
        message = twilio_client.messages.create(
            body=body,
            from_=settings.TWILIO_WHATSAPP_NUMBER,
            to=to
        )
        logger.info(f"Message sent: {message.sid}")
    except Exception as e:
        logger.error(f"Failed to send message via Twilio: {e}")
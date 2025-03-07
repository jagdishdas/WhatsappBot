from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_WHATSAPP_NUMBER: str
    CHATBOT_API_URL: str
    LLM_API_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
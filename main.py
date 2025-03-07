from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import time
from config import settings
from logger import logger
from chatbot import get_chatbot_response
from twilio_service import send_whatsapp_message
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    try:
        form_data = await request.form()
        incoming_message = form_data.get("Body", "").strip()
        sender_number = form_data.get("From", "").strip()  # e.g., "whatsapp:+923313028194"
        sender_name = form_data.get("ProfileName", "User")
        
        logger.info(f"Received WhatsApp message from {sender_number} ({sender_name}): {incoming_message}")
        
        # Get chatbot response
        start_time = time.time()
        chatbot_reply = await get_chatbot_response(incoming_message)
        chatbot_api_time = time.time() - start_time
        logger.info(f"Chatbot API response time: {chatbot_api_time:.2f} seconds")
        
        logger.info(f"Chatbot reply: {chatbot_reply}")
        
        # Send the message using Twilio client
        send_whatsapp_message(sender_number, chatbot_reply)
        
        # Create a Twilio MessagingResponse to send the chatbot reply
        twiml_response = MessagingResponse()
        twiml_response.message(chatbot_reply)
        
        # Log the TwiML response
        logger.info(f"TwiML Response: {str(twiml_response)}")
        
        # Return TwiML XML to Twilio
        return Response(content=str(twiml_response), media_type="application/xml")
    
    except Exception as e:
        logger.error(f"Error processing WhatsApp message: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
async def read_root():
    return {"message": "Server is running!"}

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting FastAPI server on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

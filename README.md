# WhatsApp Chatbot Integration via Twilio

A production-grade solution that integrates a dynamic chatbot with WhatsApp using Twilio webhooks and FastAPI. This system receives user messages on your WhatsApp business number, forwards them to a chatbot API for processing, and then delivers real-time, intelligent responses back to the user.

---

## Features

- **Real-Time Communication:** Seamlessly receive and process WhatsApp messages.
- **Dynamic Chatbot Integration:** Forward user queries to a backend chatbot API (powered by advanced models like GPT-4o Mini) and generate customized responses.
- **Twilio Sandbox Support:** Easily test your solution in a sandbox environment before moving to production.
- **Scalable Architecture:** Built on FastAPI with asynchronous processing for high performance.
- **Comprehensive Logging:** Detailed logs for monitoring and debugging message flows.

---

## How It Works

1. **Message Reception:**
   - When a user sends a WhatsApp message to your business number, Twilio receives the message and triggers a webhook.

2. **Webhook Processing:**
   - The FastAPI endpoint at `/whatsapp` parses the incoming POST request (form data with fields like `Body`, `From`, and `ProfileName`).
   - The endpoint forwards the user’s message as a JSON payload to your chatbot API (e.g., `https://chatbot-abis-8ee24a4bf8aa.herokuapp.com/query/`).

3. **Response Generation:**
   - Your chatbot API processes the query, generates an intelligent response, and returns it in JSON format (with a key `"response"`).

4. **Reply Delivery:**
   - The FastAPI endpoint builds a valid TwiML (XML) response using Twilio’s `MessagingResponse`.
   - Twilio reads this XML response and sends the reply back to the user on WhatsApp.

---

## Prerequisites

- **Python 3.8+**
- **Twilio Account:** With WhatsApp Sandbox configured.
- **Chatbot API Endpoint:** Deployed on Heroku or another hosting platform.
- **ngrok (Optional):** For exposing your local FastAPI server to the internet during development.

---

## Setup and Installation

1. Clone the repository:  
   `git clone https://github.com/<your-username>/whatsapp-chatbot.git`  
   `cd whatsapp-chatbot`  
2. Create and activate a virtual environment:  
   `python -m venv myenv`  
   (On Windows: `.\myenv\Scripts\activate` | On macOS/Linux: `source myenv/bin/activate`)  
3. Install dependencies:  
   `pip install fastapi uvicorn twilio python-dotenv httpx`  
4. Create a `.env` file in the project root with:

5. Configure your Twilio Sandbox:  
- Log in to your Twilio Console and navigate to the WhatsApp Sandbox settings.  
- Set the "When a message comes in" webhook URL to your public URL (e.g., if using ngrok, `https://<your-ngrok-url>.ngrok-free.app/whatsapp`).  
- Save the changes.

**Running the Application:**  
1. Start the FastAPI server:  
`python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000`  
2. (Optional) Expose your local server with ngrok:  
`ngrok http 8000`  
Then update your Twilio webhook with the provided ngrok URL followed by `/whatsapp`.

**Testing the Chatbot:**  
1. Join the Sandbox: Open WhatsApp and send the provided join code from your Twilio Sandbox settings to the sandbox number (typically, whatsapp:+14155238886).  
2. Send a test message from your enrolled WhatsApp number.  
3. The message will be forwarded to the FastAPI endpoint, processed by the chatbot API, and the generated reply will be sent back to your WhatsApp.

**Troubleshooting:**  
- Ensure your webhook URL is correct and includes the `/whatsapp` path.  
- Verify that your WhatsApp number is enrolled in the Twilio Sandbox.  
- Check your FastAPI and Twilio logs for errors (e.g., daily messaging limits on trial accounts).  
- If messages are not delivered, test with a static reply to isolate integration issues.

**License:**  
This project is licensed under the MIT License.



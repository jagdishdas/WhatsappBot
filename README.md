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

### 1. Clone the Repository
```bash
git clone <repository-url>
cd whatsapp-chatbot

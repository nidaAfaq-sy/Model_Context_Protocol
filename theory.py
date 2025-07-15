import os
import chainlit as cl
from dotenv import load_dotenv
import google.generativeai as genai

# ✅ Load environment variables
load_dotenv()

# ✅ Get Gemini API key
API_KEY = os.getenv('GEMINI_API_KEY')
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file.")

# ✅ Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # Or "gemini-1.5-pro"

# ✅ Chainlit message handler
@cl.on_message
async def handle_message(message: cl.Message):
    try:
        # Get response from Gemini
        gemini_response = model.generate_content(message.content)
        await cl.Message(content=gemini_response.text).send()
    except Exception as e:
        await cl.Message(content=f"❌ Error: {e}").send()

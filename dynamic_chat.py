
import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging
from vertex_chat import generate_vertex_repsonse

chat_history = []
logger = logging.getLogger("uvicorn")
def  generate_dynamic_response(search_string):
    load_dotenv()
    # Configure the API key
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)

    # Create the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-002",
    generation_config=generation_config,
    system_instruction=[
                    "You are a helpful assistant"
        ],
    )

    # Start the chat session
    chat_session = model.start_chat(history=chat_history)

    # Send message to the model
    response = chat_session.send_message(search_string)
    chat_history.extend(chat_session.history)

    # Check for the specific phrase about lacking real-time info and provide a grounded response
    if "I do not" in response.text or "I don't" in response.text or "real-time" in response.text:
        print("Grounded reesponse enabled")
        logger.info("Grounded response enabled")
        grounded_response = generate_vertex_repsonse(search_string)
        return grounded_response
    else:
        print("Normal response enabled")
        logger.info("Normal response enabled")
        return response.text

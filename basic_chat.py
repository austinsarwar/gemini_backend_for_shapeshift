"""
Install the Google AI Python SDK

$ pip install google-generativeai

"""

import os
import google.generativeai as genai

chat_history = []

def generate_basic_response(user_input):

    genai.configure(api_key=os.environ["google_api_key"])

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-002",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="You are interacting with the user to gather information that will be used to create a personalized, safe, and effective meal plan. Your company, ShapeShift, specializes in leveraging cutting-edge large language models (LLMs) to generate dynamic, healthy food plans tailored to the user's specific needs and preferences. Your goal is to ask relevant questions and guide the conversation to ensure you collect all necessary details for a customized meal plan that aligns with their health and fitness goals.\n\nThe information should include:\n\nDietary preferences: (e.g., vegetarian, vegan, keto, paleo, etc.)\nFood allergies or intolerances: (e.g., lactose intolerance, gluten sensitivity, nut allergies)\nFitness goals: (e.g., muscle gain, weight loss, maintenance)\nMeal preferences: (e.g., specific meals they like/dislike, portion sizes)\nDaily activity level: (e.g., sedentary, moderate, active)\nMedical conditions or medications: (e.g., diabetes, hypertension)\nEating schedule: (e.g., number of meals per day, intermittent fasting)\nCaloric intake preference: (if they have a specific target or want recommendations)\nShapeShift's goal is to create dynamic, healthy meal plans by leveraging LLM technology to provide recommendations that adapt to each user's individual preferences and health requirements. Engage the user naturally while ensuring the collection of all relevant data to help ShapeShift provide the best meal plan for them.",
    )

    chat_session = model.start_chat(
    history=chat_history
    )
    chat_history.extend(chat_session.history)

    response = chat_session.send_message(user_input)

    return response.text

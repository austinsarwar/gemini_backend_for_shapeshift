"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai


def generate_meal_plan():
      load_dotenv()
      genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

      # Create the model
      generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
      }

      model = genai.GenerativeModel(
        system_instruction="""
        Generate a one-day meal plan in markdown format. The meal plan should include:
        - **Breakfast**, **Lunch**, **Dinner**, and **Snacks**.
        - Each meal should have a brief description, and list of ingredients.
        - Include approximate calorie counts for each meal.

        Example markdown structure:
        
        # 1-Day Meal Plan

        ## Breakfast
        - **Dish:** <Dish Name>
        - **Description:** <Brief description>
        - **Ingredients:** <List ingredients>
        - **Calories:** <Approximate calories>

        ## Lunch
        ...

        ## Snacks
        ...
        
        ## Dinner
            

        """.strip(),
        model_name="gemini-1.5-flash-002",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
      )

      chat_session = model.start_chat(
      
      )

      response = chat_session.send_message("Send meal plan")
      print(response.text)
      return response.text

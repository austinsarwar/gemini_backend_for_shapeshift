from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import base64
from pathlib import Path
import os
from dynamic_chat import generate_dynamic_response
from openai_mealplan import generate_mealplan
from basic_chat import generate_basic_chat
from dotenv import load_dotenv
# To start with live reload use command uvicorn fastAPI_gemini:app --reload

load_dotenv()
# Check if GOOGLE_CREDENTIALS (base64-encoded key) is present
base64_key = os.getenv("GOOGLE_CREDENTIALS")


# Get the current directory path
current_directory = Path(__file__).parent

# Use a relative path for local development
key_file_path = current_directory / "service-account-key.json"

if base64_key:
    # Decode the base64 string and save it as JSON
    key_json = base64.b64decode(base64_key).decode('utf-8')
    with open(key_file_path, 'w') as f:
        f.write(key_json)

    # Set GOOGLE_APPLICATION_CREDENTIALS to the newly created JSON file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(key_file_path)
else:
    # If GOOGLE_CREDENTIALS is not set, ensure GOOGLE_APPLICATION_CREDENTIALS is correctly pointing to the file
    service_account_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not service_account_path:
        print("Error: No credentials set!")


        
app = FastAPI()



conversation_history = ""

origins = [
    "http://localhost:3000",  # Add this origin
    "http://localhost:5173",  # Ensure this has the full URL
    "http://localhost:5174",
    "http://127.0.0.1:5173", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"Message:", "Hello World"}

@app.get("/dynamic_chat/{query}") # chat with llm with dynamic vertex use. for paid users only because of high cost.
async def  dynamic_response(query):
     return generate_dynamic_response(query)
     
@app.get("/meal_plan") # Create a meal plan based off of user input
async def generate_meals():
    return generate_mealplan()

@app.get("/basic_chat/{query}" ) # basic chat with an llm use flash model only. can be used with free tier. 
async def basic_response(query):
    return generate_basic_chat(query)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 5000))  # Get port from Heroku
    uvicorn.run(app, host="0.0.0.0", port=port)
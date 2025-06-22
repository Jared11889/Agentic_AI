import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main(argv):
    #Check for argument
    if len(argv) <= 1:
        print("Please provide a prompt.")
        sys.exit(1)
    else:
        user_prompt = argv[1]
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

main(sys.argv)
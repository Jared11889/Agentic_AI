import sys
import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main(args):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__": 
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("user_prompt")
    arg_parser.add_argument("--verbose", action="store_true")
    args = arg_parser.parse_args()

    #Check for prompt
    if len(args.user_prompt) < 1:
        print("Please provide a prompt.")
        sys.exit(1)
    else:
        main(args)
else:
    print("Please run from main.py")
    sys.exit(1)
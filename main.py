import sys
import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import *


def main(args):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[get_available_functions()],
            system_instruction=system_prompt
        )
    )

    print(response.text)
    if response.function_calls:
        print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")
        result = call_function(response.function_calls[0])
        if result.parts[0].function_response.response:
            print(f"-> {result.parts[0].function_response.response["result"]}")
        else:
            raise Exception("Unknown Function")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            

if __name__ == "__main__": 
    #Check for prompt
    if not sys.argv or sys.argv[0][0] == "-":
        print("Please provide a prompt.")
        sys.exit(1)        

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("user_prompt")
    arg_parser.add_argument("--verbose", "--Verbose", "--VERBOSE", action="store_true")
    args = arg_parser.parse_args()

    main(args)
else:
    print("Please run from main.py")
    sys.exit(1)
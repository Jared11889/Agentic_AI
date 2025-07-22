import sys
import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

from config import MAX_ITERATIONS
from prompts import system_prompt
from call_function import *


def main():
    #Check for prompt and parse args
    if not sys.argv or sys.argv[0][0] == "-":
        print("Please provide a prompt.")
        sys.exit(1)        
    else:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("user_prompt")
        arg_parser.add_argument("--verbose", "--Verbose", "--VERBOSE", action="store_true")
        args = arg_parser.parse_args()

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    i = 0
    while True:
        i += 1
        if i > MAX_ITERATIONS:
            print(f"Maximum iterations ({MAX_ITERATIONS}) reached.")
            sys.exit(1)  

        try:
            response = generate_content(client, messages, args.verbose)
            if response:
                print("Final Response:")
                print(response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
       

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[get_available_functions()],
            system_instruction=system_prompt
        )
    )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text
    
    function_responses = []
    for function_call in response.function_calls:
        function_result = call_function(function_call, verbose)
        if not function_result.parts or not function_result.parts[0].function_response:
            raise Exception("empty function call result")
        
        if verbose:
            print(f"-> {function_result.parts[0].function_response.response}")
        function_responses.append(function_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    messages.append(types.Content(role="tool", parts=function_responses))
    


if __name__ == "__main__":
    main()
else:
    print("Please run from main.py")
    sys.exit(1)
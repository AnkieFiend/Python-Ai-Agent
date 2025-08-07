import os
from dotenv import load_dotenv
import sys
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(model='gemini-2.0-flash-001', contents= sys.argv)




def main():
    print("Hello from ai-agent-build!")
    if len(sys.argv) < 2:
        print("error: please provide a prompt",  file = sys.stderr)
        sys.exit(1)
    elif len(sys.argv) >= 2:
        print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



if __name__ == "__main__":
    main()

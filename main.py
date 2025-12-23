import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentResponse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# def promt_decorator(func):
#     def wrapper(*args,**kwargs):
#         print(f"User prompt:{args}")
#         return func(*args,**kwargs)
#     return wrapper
#
# @promt_decorator


def promt(promt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=promt,
    )
    # print(response.usage_metadata)
    # print(response.text)
    return response


def printer(input: str, response: GenerateContentResponse):
    print(f"User prompt: {input}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)


def main():
    input = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = promt(input)
    printer(input, response)


if __name__ == "__main__":
    main()


"""
cache_tokens_details=None
cached_content_token_count=None
candidates_token_count=100
candidates_tokens_details=None
prompt_token_count=20 
prompt_tokens_details=[ModalityTokenCount(modality=<MediaModality.TEXT: 'TEXT'>, token_count=20)]
thoughts_token_count=1108
tool_use_prompt_token_count=None
tool_use_prompt_tokens_details=None
total_token_count=1228
traffic_type=None
"""

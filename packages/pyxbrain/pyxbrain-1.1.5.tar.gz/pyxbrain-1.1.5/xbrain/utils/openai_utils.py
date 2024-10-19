from xbrain.utils.config import Config
from openai import OpenAI
import openai


system_prompt = """
{prompt_user}
"""


def chat(messages, tools=None, user_prompt="", response_format=None):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    formatted_prompt = system_prompt.format(
        prompt_user=user_prompt
    )
    messages = [{"role": "system", "content": formatted_prompt}] + messages
    response = client.beta.chat.completions.parse(
        model=config.OPENAI_MODEL,
        messages=messages,
        temperature=0.1,
        **({"response_format": response_format} if response_format is not None else {}),
        **({"tools": [openai.pydantic_function_tool(tool) for tool in tools]} if tools is not None else {}),
    )
    message = response.choices[0].message
    return message

from openai import OpenAI

from .prompt import CHECK_ODD_PROMPT
from .response_format import IsOddResponse

client = OpenAI()
def is_odd(n: int, model: str = "gpt-4o-mini") -> bool:
    """
    Check if a number is odd using LLM.

    Args:
        n (int): The number to check.
        model (str): The model to use. Defaults to "gpt-4o-mini".

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    response = client.beta.chat.completions.parse(
        model=model,
        messages=[{"role": "user", "content": CHECK_ODD_PROMPT.format(number=n)}],
        response_format=IsOddResponse,
    )
    return response.choices[0].message.parsed.is_odd

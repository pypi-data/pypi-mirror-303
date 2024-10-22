# is-odd-llm

LLM is so powerful 💪, let's use it to check if a number is odd.

Inspired by [is-odd-ai](https://github.com/rhettlunn/is-odd-ai). So I build a Python version of it.

## Install

```bash
pip install is-odd-llm
```

## Usage

set up your OpenAI API key in the environment variable `OPENAI_API_KEY`

```bash
export OPENAI_API_KEY="sk-..."
```

then you can use the `is_odd` function to check if a number is odd.

### Example

```python
from is_odd_llm import is_odd

print(is_odd(1))  # high probability is True
print(is_odd(2))  # high probability is False
```

## Contributing

Feel free to open an issue or a PR or any other suggestions.

## License

[MIT](LICENSE)

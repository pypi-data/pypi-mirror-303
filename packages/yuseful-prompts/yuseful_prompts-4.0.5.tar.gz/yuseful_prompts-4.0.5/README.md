# yuseful_prompts

## what is this ?

This is a simple python package that uses `ollama` with prompts I'm finding useful for my Markets Agent project. It is meant to run LLM intelligence that can fit a 20GB VRAM GPU with acceptable speed.

## pre requisites

- `ollama` installed with a model of your chosing referenced in as the `DEFAULT_MODEL` in `yuseful_prompts/llms.py`
- a working Python 3.12+ installation with `venv` installed

## Running Tests

To run the tests, follow these steps:

1. Ensure you have pytest installed:
   ```
   pip install pytest
   ```

2. Navigate to the project root directory.

3. Run all tests:
   ```
   pytest
   ```

4. To run tests from a specific file:
   ```
   pytest yuseful_prompts/tests/test_category_chains.py -vv -s
   pytest yuseful_prompts/tests/test_headline_chains.py -vv -s
   pytest yuseful_prompts/tests/test_misc_chains.py -vv -s
   ```

5. To run a specific test function:
   ```
   pytest tests/test_file.py::test_function_name
   ```

Make sure to replace `test_file.py` and `test_function_name` with the actual file and function names.

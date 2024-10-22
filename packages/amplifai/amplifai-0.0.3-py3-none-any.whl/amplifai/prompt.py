"""`amplifier.prompt` module.

Defines a utility function to create a formatted prompt.
"""


DEFAULT_SYSTEM_PROMPT = """You are an AI assistant specialized in identifying relevant values in a text.

You are asked to transform unstructured text into structured data. Think tabular data or a json document.
The desired structure of the ouput will be given. 
More precisely, the attributes that you need to identify and their types will be provided.
Your task is therefore to identify the values of the attributes in the text and return them in the desired format.

Please beware to follow the rules below:
ONLY extract from what is in the provided in the text, 
ALWAYS return the provided default value for the attribute's value if its value is not found in the input text. If no default value is provided, return null.
Avoid trying to perform calculations or guesses.

"""


DEFAULT_HUMAN_PROMPT = """
{text}
"""

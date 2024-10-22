"""Test to check the end-to-end functionality of the framework."""

import os

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_mistralai import ChatMistralAI
from langchain_openai import ChatOpenAI

from amplifai import Amplifier

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRALAI_API_KEY = os.getenv("MISTRALAI_API_KEY")


class Person(BaseModel):
    """A person object."""
    
    name: str
    age: int
    phone_number: str| None = None
    email_adress: str| None = None


def test_e2e_openai():
    """Test the end-to-end functionality of the OpenAI API."""
    
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")
    amplifier = Amplifier[ChatOpenAI, Person](llm=llm)
    text = "John Doe is 25 years old. He lives in Paris and can be reached at +33 6 12 34 56 78 or at firstname.name@gmail.com"
    person = amplifier.denoise(text=text)
    assert person.name == "John Doe"


def test_e2e_mistralai():
    """Test the end-to-end functionality of the MistralAI API."""
    
    llm = ChatMistralAI(api_key=MISTRALAI_API_KEY, model="mistral-large-latest")
    amplifier = Amplifier[ChatMistralAI, Person](llm=llm)
    text = "John Doe is 25 years old. He lives in Paris and can be reached at +33 6 12 34 56 78 or at firstname.name@gmail.com"
    person = amplifier.denoise(text=text)
    assert person.name == "John Doe"


def main():
    test_e2e_openai()
    test_e2e_mistralai()

if __name__ == "__main__":
    main()


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'keys')))
from keys.secret_key import openapi_key

os.environ['OpenAI_API_KEY'] = openapi_key

from langchain_openai import OpenAI

llm = OpenAI(temperature=0.7)

def generate_recipe(ingredients):
    prompt = f"Generate a recipe using the following ingredients: {', '.join(ingredients)}."
    recipe = llm(prompt)
    return recipe


result = llm("Salmon, seeaweeds. What can I make with these ingredients?")
print(result)


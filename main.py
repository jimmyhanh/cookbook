import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'keys')))
from keys.secret_key import openapi_key

os.environ['OpenAI_API_KEY'] = openapi_key
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

llm = OpenAI(temperature=0.7)

# Step 1: Get cuisine from user
cuisine = input("Enter a cuisine: ")

# Step 2: Generate ingredients
ingredient_prompt = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to make a dish that is inspired by {cuisine} cuisine. What ingredients should I use?"
)
ingredients_response = llm.invoke(ingredient_prompt.format(cuisine=cuisine))
print("\nIngredients:", ingredients_response)

# Step 3: Generate dish
dish_prompt = PromptTemplate(
    input_variables=['ingredients'],
    template="Create a step-by-step recipe using these ingredients: {ingredients}. Make sure each step is unique and do not repeat instructions."
)

dish_response = llm.invoke(dish_prompt.format(ingredients=ingredients_response))
print("\n\nRecipe:", dish_response)


from langchain.chains import SimpleSequentialChain, LLMChain

ingredient_chain = LLMChain(llm=llm, prompt=ingredient_prompt)
dish_chain = LLMChain(llm=llm, prompt=dish_prompt)

chain = SimpleSequentialChain(chains=[ingredient_chain, dish_chain])
print(chain.run(cuisine=cuisine))

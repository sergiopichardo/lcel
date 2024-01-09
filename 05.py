import os
from langchain_community.tools import DuckDuckGoSearchRun 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY")
)


search = DuckDuckGoSearchRun()

template = """Turn the following user input into a search query for a search engine:

{input}
"""


prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model | StrOutputParser() | search

result = chain.invoke({ "input": "What's the name of the oldest cat in the world?" })

print(result)


from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser

from dotenv import load_dotenv

load_dotenv()

functions = [
    {
        "name": "joke",
        "description": "A joke",
        "parameters": {
            "type": "object",
            "properties": {
                "setup": {"type": "string", "description": "The setup for the joke"},
                "punchline": {
                    "type": "string",
                    "description": "The punchline for the joke",
                },
            },
            "required": ["setup", "punchline"],
        },
    }
]

prompt = ChatPromptTemplate.from_template("tell me a joke about {input}")
model = ChatOpenAI()


chain = (
    prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonOutputFunctionsParser()
)

print(chain.invoke({ "input": "bears"}, config={}))


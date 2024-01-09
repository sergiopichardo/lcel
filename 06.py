from operator import itemgetter
from langchain.schema.runnable import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

def length_function(text): 
    return len(text)

def _multiple_length_function(text1, text2):
    return len(text1) * len(text2)

def multiple_length_function(_dict):
    return _multiple_length_function(_dict["text1"], _dict["text2"])

prompt = ChatPromptTemplate.from_template("What is {a} + {b}")


chain = {
    "a": itemgetter("foo") | RunnableLambda(length_function), # len("bar") = 3
    "b": {
        "text1": itemgetter("foo"), # "bar"
        "text2": itemgetter("bar")  # "gah"
    } | RunnableLambda(multiple_length_function) # len("bar") * len("gah") = 3 * 3 = 9
} | prompt | model | StrOutputParser() 

result = chain.invoke({ "foo": "bar", "bar": "gah" })

print(result)




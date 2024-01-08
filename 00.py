import os 
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(openai_api_key="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")
prompt = ChatPromptTemplate.from_template("tell me a joke about {input}")


chain = prompt | llm | StrOutputParser()

chain.invoke({ "input": "spices" })


bound_chain = prompt | llm.bind(stop=["\n"]) | StrOutputParser()
bound_chain.invoke({ "input": "vegetables" })
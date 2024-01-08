import os 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma 
from langchain.schema.runnable import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# from langchain_community.embeddings import OpenAIEmbeddings <-- NOTE: This way is deprecated 



text = [
    "Cats are typically 9.1 kg in weight",
    "Cats have retractable claws",
    "A group of cats is called a clowder",
    "Cats can rotate their ears 180 degrees",
    "The world's oldest cat lived to be 38 years old.",
]

llm = ChatOpenAI()

vectorstore = Chroma.from_texts(text, embedding=OpenAIEmbeddings())

retriever = vectorstore.as_retriever()

template = """Answer the question based on the following context:
{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt 
    | llm 
    | StrOutputParser()
)

result = chain.invoke("how old is the oldest cat?")

"""
Why do we need `RunnablePassthrough`?
- The `RunnablePassthrough()` function fetches the question we pass to `chain.invoke()` and embeds it in the dictionary we pass to `prompt`. 

"""

print(result)
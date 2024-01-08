from operator import itemgetter
# from langchain.schema.runnable import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma 
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

template = """
Answer the question based only on the following context: {context}

Question: {question}

Answer in the following language: {language}
"""

text = [
    "Cats are typically 9.1 kg in weight",
    "Cats have retractable claws",
    "A group of cats is called a clowder",
    "Cats can rotate their ears 180 degrees",
    "The world's oldest cat lived to be 38 years old.",
]

model = ChatOpenAI()

prompt = ChatPromptTemplate.from_template(template)

vectorstore = Chroma.from_texts(text, embedding=OpenAIEmbeddings())

retriever = vectorstore.as_retriever()

# chain = {
#     "context": itemgetter("question") | retriever,
#     "question": itemgetter("question"),
#     "language": itemgetter("language")
# } | prompt | model | StrOutputParser()

chain = {
    "context": (lambda x: x["question"]) | retriever,
    "question": (lambda x: x["question"]),
    "language": (lambda x: x["language"])
} | prompt | model | StrOutputParser()


result = chain.invoke({ 
    "question": "how old is the oldest cast?",
    "language": "Spanish"
})


print("result:", result)




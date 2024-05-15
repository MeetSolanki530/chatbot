from langchain_openai import  ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser #Default output parser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

### Langsmith tracking
os.environ["LANGCHAIN_TRACING_V1"] = "True"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title("Langchain Demo with OLLAMA SERVER")
input_text = st.text_input("Seach Anything")

# OpenAI LLM

llm = Ollama(model="llama3")
output_parser=StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question' : input_text}))



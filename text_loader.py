from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

llm=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

prompt=PromptTemplate(
    template='Write a summary for the following poem \n {poem}',
    input_variables=['poem']
)
parser=StrOutputParser()



loader=TextLoader('poem.txt')

docs=loader.load()
print(type(docs))
print(len(docs))
print(docs[0])
print(type(docs[0]))

chain=prompt |llm |parser
print(chain.invoke({'poem':docs[0].page_content}))
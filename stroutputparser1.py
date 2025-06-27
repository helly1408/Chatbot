from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

llm=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
template1=PromptTemplate(
    template='Write a detailed report on the {topic}',
    input_variables=['topic']
)
template2=PromptTemplate(
    template='Write 5 line summary on the following {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain=template1 | llm |parser | template2 | llm |parser
result= chain.invoke({'topic':'Taj Mahal'})
print(result)


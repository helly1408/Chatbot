from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import os
load_dotenv()
llm=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

class Person(BaseModel):
    name:str=Field(description='Name of the person')
    age:int= Field (gt=18,description='Age of the person')        
    city:str=Field(description='Name of the city person belongs to')   

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Generate name,age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain=template |llm |parser
result=chain.invoke({'place':'American'})
print(result)
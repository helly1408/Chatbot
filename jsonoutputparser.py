from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
load_dotenv()
llm=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
parser=JsonOutputParser()
 
template=PromptTemplate(
    template='Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[], 
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain=template | llm | parser
result=chain.invoke({})
print(result)
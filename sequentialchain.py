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

prompt1=PromptTemplate(
    template='Generate a detailed report on{topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain=prompt1 | llm |parser | prompt2 | llm | parser
result=chain.invoke({'topic':'Cricket'})
print(result)
chain.get_graph().print_ascii()

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
import os
load_dotenv()

llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
parser=StrOutputParser()
class Feedback(BaseModel):
    sentiment:Literal['positive','negative'] = Field(description='Give the sentiment of the feedbcak')

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template='Classify the sentiment of the follwoing text into positive or negative \n {feedback}\n{format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)
classifier_chain=prompt1 | llm |parser2

prompt2=PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='Write an appropriate response to this negative k \n {feedback}',
    input_variables=['feedback']
)


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | llm | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | llm | parser),
    RunnableLambda(lambda x: "Could not determine sentiment.")
)


chain=classifier_chain | branch_chain
print(chain.invoke({'feedback':'The weather is very beautiful.'}))
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from src.Tools.tools import web_search, extract_content_from_url
import os

load_dotenv()


model = ChatOpenAI(model="gpt-5.4-mini", temperature=0, openai_api_key=os.getenv("OPENAI-API-KEY"))

def create_search_agent():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a research assistant that helps users find information on a topic. You have access to the following tools: web_search . Use these tools to find relevant information and answer the user's question."),
        ("human", "{input}")
    ])
    
    agent = create_agent(
        model, tools=[web_search]
    
    )
    
    return agent

def reader_agent():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a research assistant that scraps web pages for relevant information. You have access to the following tools:  extract_content_from_url. Use these tools to find relevant information and answer the user's question."),
    ])
    
    agent = create_agent(
         model, 
        tools=[extract_content_from_url]
    
    )
    
    return agent

#Writer Chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant that helps users find information on a topic. You have access to the following tools: web_search and extract_content_from_url. Use these tools to find relevant information and answer the user's question."),
    ("human", """Write a comprehensive research report on the topic of {topic}.
           Use the following information as a basis for your report: {information}. Make sure to cite your sources and provide a well-structured report with an introduction, main body, and conclusion. 
     Topic: {topic}
     Information: {information}
     Structure: The report should be well-structured with an introduction, main body, and conclusion. The introduction should provide an overview of the topic and its significance. The main body should delve into the details, providing evidence and analysis to support the points made. The conclusion should summarize the key findings and their implications.
        
     
     The report should be detailed and cover all relevant aspects of the topic."""),        
])

WriterChain = writer_prompt | model | StrOutputParser()

#Critic Chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant that helps users find information on a topic. You have access to the following tools: web_search and extract_content_from_url. Use these tools to find relevant information and answer the user's question."),
    ("human", """Critique the following research report on the topic of {topic}.
           The report is as follows: {report}. Provide constructive feedback on the content, structure, and clarity of the report. Highlight any areas that need improvement and suggest ways to enhance the overall quality of the report. 
     Topic: {topic}
     Report: {report}
     Feedback: The feedback should be constructive and specific, addressing both strengths and weaknesses of the report. It should provide actionable suggestions for improvement, such as clarifying certain points, adding more evidence, or improving the structure of the report.
        
     
     The critique should be detailed and provide valuable insights for improving the research report."""),        
])
CriticChain = critic_prompt | model | StrOutputParser()



from  src.Agents.agents import CriticChain, create_search_agent, reader_agent, WriterChain, critic_prompt
from src.Tools.tools import web_search, extract_content_from_url

def research_pipeline( topic: str) -> str:
    state = {}

    #search Agent 
    print("/n/nExecuting Search Agent...")

    search_agent = create_search_agent()
    search_results = search_agent.invoke({"messages": [{"role": "user", "content": f"Find recent and reliable information on the : {topic}"}]})
    state['search_results'] = search_results['messages'][-1].content

    
    print(state['search_results'])
    
    #reader Agent
    print("/n/nExecuting Reader Agent...")
    reader_agent_instance = reader_agent()
    reader_results = reader_agent_instance.invoke({"messages": [{"role": "user", "content": f"Extract relevant information from the following search results: {state['search_results']}"}]})
    state['reader_results'] = reader_results['messages'][-1].content    
    print(state['reader_results'])

    #Writer Agent
    print("/n/nExecuting Writer Agent...")

    Research_Combined = f"Topic: {topic}\n\nSearch Results: {state['search_results']}\n\nExtracted Information: {state['reader_results']}"
    state['report'] = WriterChain.invoke({"topic": topic, "information": Research_Combined})
    print(f"\nGenerated Report:\n{state['report']}")

    return state['report']

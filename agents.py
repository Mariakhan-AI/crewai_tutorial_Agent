import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent

# Ensure there's an event loop in the current thread
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Create LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.7
)

# Agents
news_researcher = Agent(
    role="News Researcher",
    goal="Research the latest news about the given topic",
    backstory="You are an expert researcher who can find the latest and most relevant information on any topic.",
    llm=llm
)

news_writer = Agent(
    role="News Writer",
    goal="Write a compelling news article based on research",
    backstory="You are a professional journalist skilled at writing engaging and clear articles.",
    llm=llm
)

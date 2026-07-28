from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="models/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5,
)

news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation, "
        "eager to explore and share knowledge that could change the world."
    ),
    verbose=True,
    memory=False,
    tools=[tool],
    llm=llm,
    allow_delegation=True,
)

news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging "
        "stories that educate and inspire readers."
    ),
    verbose=True,
    memory=False,
    tools=[tool],
    llm=llm,
    allow_delegation=False,
)
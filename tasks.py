from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

research_task = Task(
    description=(
        "Identify the next big trend in {topic}. "
        "Focus on identifying pros and cons and the overall narrative."
    ),
    expected_output="A 3 paragraph report.",
    tools=[tool],
    agent=news_researcher,
)

write_task = Task(
    description=(
        "Write an engaging article about {topic} "
        "using the research report."
    ),
    expected_output="Markdown article.",
    tools=[tool],
    agent=news_writer,
    output_file="new-blog-post.md",
)
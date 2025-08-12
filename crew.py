from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer

# Create crew without persistent memory (avoids ChromaDB)
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=False  # ✅ disables ChromaDB / embedchain usage
)

if __name__ == "__main__":
    result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
    print(result)

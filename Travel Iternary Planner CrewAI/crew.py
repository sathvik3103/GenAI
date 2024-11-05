# main.py
from crewai import Crew, Agent, Task, Process
from agents import ResearchAgent, WeatherAnalysisAgent, WeatherAnalysisAgent, BudgetOptimizationAgent, RecommendationAgent
from tasks import ResearchDestinationTask, AnalyzeWeatherTask, CreateItineraryTask, OptimizeBudgetTask, GenerateRecommendationsTask

    # Create crew
crew = Crew(
        agents=[ResearchAgent, WeatherAnalysisAgent, WeatherAnalysisAgent, BudgetOptimizationAgent, RecommendationAgent],
        tasks=[ResearchDestinationTask, AnalyzeWeatherTask, CreateItineraryTask, OptimizeBudgetTask, GenerateRecommendationsTask]
    )

    # Execute the crew's plan
result = crew.kickoff(inputs={'topic':'AI in Education'})

print(result)
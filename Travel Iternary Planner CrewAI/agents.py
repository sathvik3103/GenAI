from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))


class ResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Research Agent",
            role="Travel Researcher",
            goal="Gather comprehensive information about travel destinations",
            backstory="An experienced travel researcher with extensive knowledge of global destinations",
            verbose=True,
            allow_delegation=False,
            tools=[
                tool
            ]
        )

class WeatherAnalysisAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Weather Analysis Agent",
            role="Meteorologist",
            goal="Provide accurate weather forecasts for travel dates",
            backstory="A skilled meteorologist specializing in travel weather forecasting",
            verbose=True,
            allow_delegation=False,
            tools=[
                tool
            ]
        )

class ItineraryCreationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Itinerary Creation Agent",
            role="Travel Planner",
            goal="Develop detailed day-by-day travel itineraries",
            backstory="An expert travel planner with a knack for creating perfect itineraries",
            verbose=True,
            allow_delegation=True,
            tools=[
                tool
            ]
        )

class BudgetOptimizationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Budget Optimization Agent",
            role="Travel Budget Specialist",
            goal="Optimize travel plans to fit within specified budgets",
            backstory="A savvy budget specialist who knows how to make the most of travel funds",
            verbose=True,
            allow_delegation=False,
            tools=[
                tool
            ]
        )

class RecommendationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Recommendation Agent",
            role="Personalized Travel Advisor",
            goal="Provide tailored recommendations for activities and experiences",
            backstory="A well-traveled advisor with a passion for creating unique travel experiences",
            verbose=True,
            allow_delegation=True,
            tools=[
                tool
            ]
        )
from crewai import Task
from tools import tool
from agents import ResearchAgent, WeatherAnalysisAgent, ItineraryCreationAgent, BudgetOptimizationAgent, RecommendationAgent


# Research Destination Task
research_destination_task = Task(
    description=(
        "Research comprehensive information about Paris. "
        "Focus on popular attractions, local customs, best times to visit, "
        "and general travel tips. Your final report should provide a clear "
        "overview of what travelers can expect."
    ),
    expected_output="A detailed 3-paragraph report on Paris, covering key attractions, cultural insights, and practical travel advice.",
    tools=[
                tool
            ],
    agent=ResearchAgent(),
)

# Analyze Weather Task
analyze_weather_task = Task(
    description=(
        "Analyze weather patterns for Paris during the travel dates: 12/5/2024 to 12/5/2024. "
        "Provide a detailed forecast including temperature ranges, precipitation probabilities, "
        "and any weather-related travel advisories."
    ),
    expected_output="A comprehensive day-by-day weather report for the entire trip duration, with recommendations on appropriate clothing and activities.",
    tools=[
                tool
            ],
    agent=WeatherAnalysisAgent(),
)

# Create Itinerary Task
create_itinerary_task = Task(
    description=(
        "Create a 5-day itinerary for Paris. "
        "Include a mix of popular attractions and off-the-beaten-path experiences. "
        "Consider travel times between locations and allow for rest periods."
    ),
    expected_output="A detailed day-by-day itinerary with suggested activities, attractions, and time allocations, formatted as a markdown list.",
    tools=[
                tool
            ],
    agent=ItineraryCreationAgent(),
)

# Optimize Budget Task
optimize_budget_task = Task(
    description=(
        "Optimize a budget of $5000 for a 5-day trip to Paris. "
        "Provide a breakdown of suggested spending for accommodation, food, activities, and transportation. "
        "Include tips for saving money and getting the best value."
    ),
    expected_output="A comprehensive budget plan with detailed allocations for each category, including money-saving tips and budget-friendly recommendations.",
    ttools=[
                tool
            ],
    agent=BudgetOptimizationAgent(),
)

# Generate Recommendations Task
generate_recommendations_task = Task(
    description=(
        "Generate personalized recommendations for Paris. Focus on unique experiences"
    ),
    expected_output="A list of at least 5 personalized activity and dining recommendations, each with a brief description and why it's a good fit for the traveler.",
    tools=[
                tool
            ],
    agent=RecommendationAgent(),
)
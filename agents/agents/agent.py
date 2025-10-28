import os
from google.adk.agents import LlmAgent

# Try to load .env file if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MODEL = "gemini-2.0-flash"

idea_agent = LlmAgent(
    model=MODEL,
    name="IdeaAgent",
    description="Brainstorms creative and exciting weekend travel ideas based on user preferences or requests.",
    instruction="You are a creative travel agent. Brainstorm and respond to the user with 3 exciting weekend trip ideas based on the user's request. Use your knowledge to provide realistic and interesting suggestions.",
    # Note: Removed google_search tool temporarily due to model compatibility
    disallow_transfer_to_peers=True,
)

refiner_agent = LlmAgent(
    model=MODEL,
    name="RefinerAgent",
    description="Reviews provided travel ideas and selects only those estimated to cost under the provided budget for a weekend trip.",
    instruction="Review the provided trip ideas and estimate costs. Respond ONLY with the ideas likely under the provided budget for a weekend. If none seem to fit, say so.",
    # Note: Removed google_search tool temporarily due to model compatibility
    disallow_transfer_to_peers=True,
)

root_agent = LlmAgent(
    model=MODEL,
    name="PlannerAgent",
    instruction="""You are a Trip Planner, coordinating specialist agents.
Your goal is to provide budget-friendly weekend trip ideas. For each user request, follow the below instructions:
1. First, use "(idea_agent)" to brainstorm ideas based on the user's request.
2. Then, use "(refiner_agent)" to take those ideas to filter them for the provided budget.
3. Present the final, refined list to the user along with the budget.""",
    sub_agents=[idea_agent, refiner_agent],
)

# Export agents for adk web
agents = [root_agent, idea_agent, refiner_agent]

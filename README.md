# Weekend Travel Planning Agent

This project contains an ADK (Agent Development Kit) multi-agent system for planning budget-friendly weekend trips.

## Architecture

The system consists of three agents:

1. **IdeaAgent** - Brainstorms creative and exciting weekend travel ideas based on user preferences
2. **RefinerAgent** - Filters travel ideas to ensure they fit within the specified budget
3. **PlannerAgent** - Coordinates the workflow between the other two agents

## Setup

### 1. Install Dependencies

Make sure you have the required dependencies installed:

```bash
pip install google-adk
```

### 2. Configure API Key

You need to provide a Google AI API key to use the Gemini models. Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

#### Option 1: Use .env file (Recommended)

1. Open the `.env` file in the project root
2. Replace `your_api_key_here` with your actual API key:

```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

The agent will automatically load the API key from the `.env` file.

#### Option 2: Set Environment Variable

```bash
export GOOGLE_API_KEY=your_api_key_here
```

## Project Structure

ADK expects a specific directory structure when running `adk web agents`:

```text
.
├── agents/
│   └── agents/
│       └── agent.py           # Main agent configuration (with root_agent)
└── requirements.txt
```

Note: When you run `adk web agents`, ADK looks for `agents/agents/agent.py`.

## Running the Agent

### Using ADK Web UI

To start the web interface, run from the project root:

```bash
adk web agents
```

This will start a web server where you can interact with your agents.

### Using ADK API Server

To start the API server:

```bash
adk api_server agents
```

### Using the Web Interface

Once `adk web agents` is running, you can:

1. Open your browser and navigate to the provided URL
2. Select the agent you want to use (PlannerAgent, IdeaAgent, or RefinerAgent)
3. Start chatting with the agent to plan your weekend trips

The `root_agent` (PlannerAgent) coordinates the workflow:

1. Calls `idea_agent` to generate travel ideas based on your request
2. Passes those ideas to `refiner_agent` to filter them by budget
3. Returns the final refined list of budget-friendly weekend trip ideas

# 🌍 AI Trip Planner: Your Intelligent Travel Assistant

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-05998b.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0+-ff4b4b.svg)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/Powered%20by-LangGraph-orange)](https://github.com/langchain-ai/langgraph)

AI Trip Planner is a sophisticated, agent-driven travel assistant that helps you plan your perfect journey. Using advanced AI orchestration (LangGraph) and high-performance LLMs (Groq), it searches for destinations, checks real-time weather, calculates expenses, and converts currencies to provide a comprehensive itinerary.

## ✨ Key Features

- **🤖 Intelligent Multi-Agent Workflow**: Powered by LangGraph for robust, stateful AI interactions.
- **📍 Smart Place Discovery**: Integrates with Tavily and other search tools to find hidden gems and top-rated spots.
- **🌦 Real-time Weather Insights**: Provides up-to-date forecasts for your travel dates.
- **💰 Expense & Currency Management**: Built-in tools for calculating trip budgets and real-time currency conversion.
- **🎨 Premium User Experience**: A stunning, modern Streamlit frontend designed for ease of use and aesthetic appeal.
- **📄 Exportable Itineraries**: Generate and download your travel plans as text files.

## 🛠 Technology Stack

- **Backend**: Python, FastAPI, LangChain, LangGraph.
- **AI Models**: Groq (Llama-3), OpenAI, or any LangChain-compatible LLM.
- **Frontend**: Streamlit with custom CSS (Premium UI).
- **Tools**: Tavily Search, Weather API, Currency Converter API.
- **Containerization**: Docker & Docker Compose.

## 📂 Project Structure

```text
├── backend/            # FastAPI application & LangGraph agents
│   ├── agent/          # Agentic logic and graph definitions
│   ├── tools/          # Custom tools (Weather, Currency, etc.)
│   ├── main.py         # Backend API entry point
│   └── Dockerfile      # Backend container config
├── frontend/           # Streamlit application
│   ├── streamlit_app.py # Premium UI implementation
│   └── Dockerfile      # Frontend container config
└── docker-compose.yml  # Multi-container orchestration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (optional but recommended)
- API Keys: Groq, Tavily (and any others required by tools)

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/AI_Trip_Planner.git
   cd AI_Trip_Planner
   ```

2. **Environment Configuration**:
   Create a `.env` file in the root directory and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   GOOGLE_API_KEY=your_google_api_key
   # Add any other keys required by your tools
   ```

3. **Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```
   - Frontend: `http://localhost:8501`
   - Backend API: `http://localhost:8000`

4. **Manual Setup (without Docker)**:
   - **Backend**:
     ```bash
     cd backend
     pip install -r requirements.txt
     python main.py
     ```
   - **Frontend**:
     ```bash
     cd frontend
     pip install -r requirements.txt
     streamlit run streamlit_app.py
     ```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Created by [Mehedi Hasan](https://github.com/Mehedi2017331043) | Empowering Travelers with AI*

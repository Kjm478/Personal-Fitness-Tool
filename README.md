# Personal Fitness Tool

A Streamlit-powered web application that leverages Retrieval-Augmented Generation (RAG), multi-AI agents, and Langflow to provide a personalized fitness management experience. Users can create and update fitness profiles, set goals, track nutrition, manage notes, and interact with AI agents for tailored advice and macro calculations.

## Features
- **Personal Data Management**: Input and update details like name, age, weight, height, gender, and activity level.
- **Goal Setting**: Choose fitness goals such as muscle gain, fat loss, or weight maintenance.
- **Nutrition Tracking**: Monitor and adjust daily calorie, protein, carb, and fat intake, enhanced by AI-generated macros.
- **Notes**: Add and delete personal notes linked to your profile, with vectorized search capabilities.
- **AI-Powered Assistance**: Engage with multi-AI agents for fitness questions and macro suggestions, powered by RAG and Langflow.

## Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/) - A Python framework for building interactive web apps with minimal effort.
- **Backend**: Python, [Astra DB](https://www.datastax.com/products/datastax-astra) (DataStax) for data storage and vector search.
- **AI Framework**: [Langflow](https://langflow.org/) - An open-source platform for orchestrating multi-AI agent workflows.
- **AI Paradigm**: Retrieval-Augmented Generation (RAG) - Combines retrieval of relevant data with generative AI for context-aware responses.
- **Dependencies**: Listed in `requirements.txt`

## How It Works
- **Streamlit**: Drives the user interface, providing an intuitive and responsive experience for managing fitness data and interacting with AI features.
- **RAG**: Enhances AI responses by retrieving relevant user data (e.g., profile and notes) from Astra DB and combining it with generative capabilities for personalized outputs.
- **Multi-AI Agents**: Powered by Langflow, the app uses distinct AI agents for tasks like answering fitness questions ("Ask AI") and generating nutrition macros ("Macros"), each fine-tuned with user-specific context.
- **Langflow**: Orchestrates the AI workflows, integrating RAG and multi-agent systems to process user inputs and deliver results via a local or hosted API.

## Prerequisites
- Python 3.12+
- Git installed locally
- A GitHub account
- Astra DB account (for database and vector storage)
- Langflow instance (local or hosted) for AI functionality

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/personal-fitness-tool.git
cd personal-fitness-tool

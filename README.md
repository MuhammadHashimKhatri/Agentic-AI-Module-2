# Gemini Agent

## Student

Muhammad Hashim

## Project

A simple AI agent built using the OpenAI Agents SDK and Google's Gemini model through Gemini's OpenAI-compatible API endpoint.

## Prerequisites

Before running this project, make sure you have:

- Git
- uv

## Setup Instructions

### 1. Install uv

If uv is not already installed, install it from:

https://docs.astral.sh/uv/getting-started/installation/

On Windows PowerShell, you can install it with:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify the installation:

```bash
uv --version
```

### 2. Clone the Repository

Clone this repository:

```bash
git clone https://github.com/MuhammadHashimKhatri/Agnetic-AI-Module-2.git
```

Move into the project folder:

```bash
cd Agnetic-AI-Module-2
```

### 3. Install Project Dependencies

Run:

```bash
uv sync
```

This will automatically create the virtual environment and install all required dependencies, including:

- openai-agents
- python-dotenv

### 4. Create the Environment File

Create a `.env` file in the project root.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Get a Gemini API key from:

https://aistudio.google.com/apikey

Do not share or commit your API key.

### 5. Run the Agent

Run the following command:

```bash
uv run src/gemini_agent/main.py
```

If everything is configured correctly, the agent will connect to Google's Gemini model and return an AI-generated response.

## Technologies

- Python
- OpenAI Agents SDK
- Google Gemini
- python-dotenv
- uv

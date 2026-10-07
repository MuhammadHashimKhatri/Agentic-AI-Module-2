from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


llm_model = OpenAIChatCompletionsModel(
    model="gemini-3.8-flash",
    openai_client = external_client
)

agent = Agent(
    name="Gemini Agent",
    model=llm_model,
)

result = Runner.run_sync(agent, "Welcome and motivate me to learn Agentic AI.")
print("AGENT RESPONSE:", result.final_output)
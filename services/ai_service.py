import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents.react.agent import create_react_agent
from langchain_classic.agents import AgentExecutor
from langchain_core.prompts import PromptTemplate
from tools.langchain_tools import product_tool, order_tool, user_tool

load_dotenv()

# LLM
llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3,
)

tools = [product_tool, order_tool, user_tool]

prompt = PromptTemplate.from_template("""
You are an AI shopping assistant.

You have access to tools:
{tools}

Available tool names:
{tool_names}

Use this format:

Question: {input}
Thought: think about what to do next
Action: one of [{tool_names}]
Action Input: input
Observation: result
... repeat ...
Final Answer: answer

Begin!

Question: {input}
Thought:{agent_scratchpad}
""")

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)


def get_ai_response(message, user_id):
    
    full_input = f"""
    User ID: {user_id}

    User message: {message}

    RULES:
    - Always use the User ID when calling user-related tools
    - For get_user_details → pass user_id
    - For get_user_orders → pass user_id
    """

    response = agent_executor.invoke({
        "input": full_input
    })

    return response["output"]

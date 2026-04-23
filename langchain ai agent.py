import os
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import gradio as gr

@tool
def calculator(expression: str) -> str:
    """Useful for solving math calculations. Input must be a valid math expression like 25 * 4 or 100 / 5"""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def word_counter(text: str) -> str:
    """Counts the number of words in a given text. Input: any sentence or paragraph."""
    count = len(text.split())
    return f"The text has {count} words."

@tool
def uppercase_tool(text: str) -> str:
    """Converts any given text to uppercase. Input: any text string."""
    return text.upper()

@tool
def lowercase_tool(text: str) -> str:
    """Converts any given text to lowercase. Input: any text string."""
    return text.lower()

@tool
def reverse_text(text: str) -> str:
    """Reverses any given text. Input: any text string."""
    return text[::-1]

@tool
def character_counter(text: str) -> str:
    """Counts the number of characters in a given text. Input: any text string."""
    return f"The text has {len(text)} characters."

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful and friendly AI assistant.
     You have the following tools available:
     - calculator: for math calculations
     - word_counter: for counting words
     - character_counter: for counting characters
     - uppercase_tool: to convert text to uppercase
     - lowercase_tool: to convert text to lowercase
     - reverse_text: to reverse any text
     
     For general knowledge questions like 'what is X', answer directly
     from your own knowledge WITHOUT using any tool.
     Only use tools when the user explicitly asks for math, word count,
     character count, or text conversion.
     Always give clear and concise answers."""),
    MessagesPlaceholder("chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])

tools = [calculator, word_counter, character_counter, uppercase_tool, lowercase_tool, reverse_text]
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=5,
    handle_parsing_errors=True
)

def run_agent(message, history):
    try:
        result = agent_executor.invoke({"input": message})
        return result["output"]
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.ChatInterface(
    fn=run_agent,
    title="🤖 LangChain AI Agent",
    description="""
    ### Welcome to LangChain AI Agent!
    I can help you with:
    - 🧮 **Calculator** — Solve any math problem
    - 📝 **Word Counter** — Count words in text
    - 🔤 **Character Counter** — Count characters
    - 🔠 **Uppercase** — Convert text to uppercase
    - 🔡 **Lowercase** — Convert text to lowercase
    - 🔁 **Reverse Text** — Reverse any text
    - 💬 **General Questions** — Ask me anything!
    """,
    examples=[
        "What is 125 * 48?",
        "What is LangChain?",
        "Count words: I am learning AI and it is very interesting",
        "Convert to uppercase: hello world",
        "Reverse this text: artificial intelligence",
        "Count characters: Hello World"
    ]
)

demo.launch(server_name="0.0.0.0", server_port=7860)
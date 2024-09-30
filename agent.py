from langchain.tools.render import format_tool_to_openai_function
from langchain_anthropic.chat_models import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, BaseMessage
from langgraph.prebuilt import ToolNode
from langchain_community.tools import IncomeStatements, BalanceSheets, CashFlowStatements
from langchain_community.utilities.financial_datasets import FinancialDatasetsAPIWrapper
from langgraph.graph import END, StateGraph, MessagesState
from langgraph.checkpoint.memory import MemorySaver
from typing import Literal, TypedDict, Annotated, Sequence
import operator

from tools import intrinsic_value, roe, roic, owner_earnings

# Set up the tools
api_wrapper = FinancialDatasetsAPIWrapper()
integration_tools = [
    IncomeStatements(api_wrapper=api_wrapper),
    BalanceSheets(api_wrapper=api_wrapper),
    CashFlowStatements(api_wrapper=api_wrapper),
]
local_tools = [intrinsic_value, roe, roic, owner_earnings]
tools = integration_tools + local_tools
tool_node = ToolNode(tools)

# Set up the LLM
gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
model = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0).bind_tools(tools)

system_prompt = """
You are an AI financial analyst with expertise in analyzing businesses using methods similar to those of Warren Buffett...
"""

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state['messages']
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END

def call_model(state: MessagesState):
    prompt = SystemMessage(content=system_prompt)
    messages = state['messages']
    if messages and messages[0].content != system_prompt:
        messages.insert(0, prompt)
    response = model.invoke(messages)
    return {"messages": [response]}

# Define the graph
workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge("tools", 'agent')
checkpointer = MemorySaver()
app = workflow.compile()
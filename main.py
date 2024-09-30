from langchain_core.messages import HumanMessage
from config import set_api_keys
from agent import app

def main():
    set_api_keys()
    final_state = app.invoke(
        {"messages": [HumanMessage(content="What was AAPL's revenue in FY 2023?")]},
        config={"configurable": {"thread_id": 42}}
    )
    print(final_state["messages"][-1].content)

if __name__ == "__main__":
    main()
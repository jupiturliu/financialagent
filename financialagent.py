from langchain_core.messages import HumanMessage

# Use the Runnable
final_state = app.invoke(
    # {"messages": [HumanMessage(content="What is NVDA's intrinsic value given a discount rate of 5%, growth rate of 10%, terminal growth rate of 3%?")]},
    {"messages": [HumanMessage(content="What was AAPL's revenue in FY 2023?")]},
    config={"configurable": {"thread_id": 42}}
)
final_state["messages"][-1].content
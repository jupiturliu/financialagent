from typing import Literal
from langgraph.graph import END, StateGraph, MessagesState


# Define the function that determines whether to continue or not
def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state['messages']
    last_message = messages[-1]
    # If the LLM makes a tool call, then we route to the "tools" node
    if last_message.tool_calls:
        return "tools"
    # Otherwise, we stop (reply to the user)
    return END

# Define the function that calls the model
def call_model(state: MessagesState):
    prompt = SystemMessage(
        content=system_prompt
    )
    # Get the messages
    messages = state['messages']

    # Check if first message in messages is the prompt
    if messages and messages[0].content != system_prompt:
        # Add the prompt to the start of the message
        messages.insert(0, prompt)

    # Call the model
    response = model.invoke(messages)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}
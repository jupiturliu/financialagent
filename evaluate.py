def predict_answer(example: dict):
    """Use this for answer evaluation"""
    question = example.get("question")

    final_state = app.invoke(
      {"messages": [HumanMessage(content=question)]},
      config={"configurable": {"thread_id": 42}}
    )
    answer = final_state["messages"][-1].content
    return {"answer": answer}


from langsmith.evaluation import LangChainStringEvaluator, evaluate

eval_llm = ChatAnthropic(temperature=0.0, model="claude-3-5-sonnet-20240620")

# Evaluator
qa_evalulator = [
    LangChainStringEvaluator(
        "qa",
        prepare_data=lambda run, example: {
            "prediction": run.outputs["answer"],
            "reference": example.outputs["answer"],
            "input": example.inputs["question"],
        },
        config={"llm": eval_llm}
      ),
]
experiment_results = evaluate(
    predict_answer,
    data=dataset_name,
    evaluators=qa_evalulator,
    experiment_prefix="financial-rag-qa",
    metadata={
      "version": "1.0.0",
      "revision_id": "beta"
    },
)
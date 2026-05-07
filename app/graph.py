from langgraph.graph import StateGraph, END

from app.state import AgentState

from app.nodes import (classifier_node, theory_node, code_node)

workflow = StateGraph(AgentState)

workflow.add_node("classifier", classifier_node)
workflow.add_node("theory", theory_node)
workflow.add_node("code", code_node)

workflow.set_entry_point("classifier")

def router(state):
    if state["question_type"] == "THEORY":
        return "theory"
    elif state["question_type"] == "CODE":
        return "code"
    else:
        raise ValueError("Invalid question type")
    
workflow.add_conditional_edges("classifier", router)

workflow.add_edge("theory", END)
workflow.add_edge("code", END)

## graph completed

##  Final step compile it 

graph = workflow.compile()
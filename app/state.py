#Defines dictionary with fixed keys and types is called as TypedDict
from typing import TypedDict

class AgentState(TypedDict):
    question: str
    question_type: str
    answer: str
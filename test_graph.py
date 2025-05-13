from typing_extensions import TypedDict, Literal
from Ipython.display import display, Image
from langraph.graph import StateGraph, START, END
import random

money = random.randint(0, 100)

# Define State of the graph
class AccountBalance(TypedDict):
    account: str
    balance: float


# Nodes
def node_1(account):
    print("--Node 1--")
    return {"balance": account.balance } 

def node_2(account):    
    print("--Node 2--")
    return {"balance": account.balance}

def node_3(account):   
    print("--Node 3--")
    return {"balance": account.balance}


# Check Account Balance
def check_account_balance(account) -> Literal["node_2", "node_3"]:
    
    balance_from_bank = account["balance"]

    if money < 100:
        print("Account is overdrawn")
        return "node_2"
    else:
        print("Account is in good standing")
        return "node_3"
    

# Build Graph 
builder = StateGraph(AccountBalance)
builder.add_node(START, node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# Logic 
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", check_account_balance)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# Compile
graph = builder.compile()
display(Image(graph.get_graph().draw_mermaid_png()))
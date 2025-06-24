from pair_programming.utils import open_ai

chat = open_ai.NewOpenAIClient()

# select a model here
models = open_ai.select_model(client=chat, prefixes=["gemma"])
print(f"models: \n{models}")
model = models[0].id
print(f"selected: \n{model}")

priming = "You are an expert at writing clear, concise, Python code."
question = """
class Node:
  def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None

class SLinkedList:
  def __init__(self):
    self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3

"""

# Simplify the code
# option 1
prompt_template = """
{priming}

Can you please simplify this code for a linked list in Python?

{question}

Explain in detail what you did to modify it, and why.
"""

prompt = prompt_template.format(priming=priming, question=question)
print(f"prompt 1:\n {prompt}")
response = open_ai.get_completion(client=chat, prompt=prompt, model=model)
print(f"response:\n {response}")
print(f"=================================================================================================")

# option 2
prompt_template = """
{priming}

Can you please simplify this code for a linked list in Python?

{question}

Please comment each line in detail, \n
and explain in detail what you did to modify it, and why.
"""

prompt = prompt_template.format(priming=priming, question=question)
print(f"prompt 2:\n {prompt}")
response = open_ai.get_completion(client=chat, prompt=prompt, model=model)
print(f"response:\n {response}")
print(f"=================================================================================================")

from pair_programming.utils import open_ai

chat = open_ai.NewOpenAIClient()

# select a model here
models = open_ai.select_model(client=chat, prefixes=["gemma"])
print(f"models: \n{models}")
model = models[0].id
print(f"selected: \n{model}")

# Note that the code I'm using here was output in the previous
# section. Your output code may be different.
question = """
class Node:
  def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None

class SLinkedList:
  def __init__(self):
    self.head = None

def create_linked_list(data):
  head = Node(data[0])
  for i in range(1, len(data)):
    node = Node(data[i])
    node.nextval = head
    head = node
  return head

list1 = create_linked_list(["Mon", "Tue", "Wed"])
"""

prompt_template = """
Can you please create test cases in code for this Python code?

{question}

Explain in detail what these test cases are designed to achieve.
"""

prompt = prompt_template.format(question=question)
print(f"prompt:\n {prompt}")
response = open_ai.get_completion(client=chat, prompt=prompt, model=model)
print(f"response:\n {response}")
print(f"=================================================================================================")

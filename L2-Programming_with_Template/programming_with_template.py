from pair_programming.utils import open_ai

chat = open_ai.NewOpenAIClient()

# select a model here
models = open_ai.select_model(client=chat, prefixes=["gemma"])
print(f"models: \n{models}")
model = models[0].id
print(f"selected: \n{model}")

prompt_template = """
{priming}

{question}

{decorator}

Your solution:
"""

priming_text = "You are an expert at writing clear, concise, Python code."
question = "create a doubly linked list"
# option 1
# decorator = "Work through it step by step, and show your work. One step per line."

# option 2
decorator = "Insert comments for each line of code."

prompt = prompt_template.format(priming=priming_text, question=question, decorator=decorator)

print(f"prompt:\n {prompt}")
response = open_ai.get_completion(client=chat, prompt=prompt, model=model)
print(f"response:\n {response}")
print(f"=================================================================================================")
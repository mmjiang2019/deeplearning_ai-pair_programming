from pair_programming.utils import open_ai

chat = open_ai.NewOpenAIClient()

# select a model here
models = open_ai.select_model(client=chat, prefixes=["gemma"])
print(f"models: \n{models}")
model = models[0].id
print(f"selected: \n{model}")

priming = "You are an expert at writing clear, concise, Python code."
question = """
def func_x(array)
  for i in range(len(array)):
    print(array[i])
"""

# Rewrite your code
prompt_template = """
{priming}

I don't think this code is the best way to do it in Python, can you help me?

{question}

Please explain, in detail, what would you do to improve it.
"""

prompt = prompt_template.format(priming=priming, question=question)
print(f"prompt:\n {prompt}")
response = open_ai.get_completion(client=chat, prompt=prompt, model=model)
print(f"response:\n {response}")
print(f"=================================================================================================")

# multiple ways of rewriting your code
prompt_template = """
{priming}

I don't think this code is the best way to do it in Python, can you help me?

{question}

Please explore multiple ways of solving the problem, and explain each.
"""

prompt = prompt_template.format(priming=priming, question=question)
print(f"prompt:\n {prompt}")
response = open_ai.get_completion(client=chat, prompt=prompt, model=model)
print(f"response:\n {response}")
print(f"=================================================================================================")

# Recommend one of the methods as most 'Pythonic'
prompt_template = """
{priming}

I don't think this code is the best way to do it in Python, can you help me?

{question}

Please explore multiple ways of solving the problem, 
and tell me which is the most Pythonic
"""

prompt = prompt_template.format(priming=priming, question=question)
print(f"prompt:\n {prompt}")
response = open_ai.get_completion(client=chat, prompt=prompt, model=model)
print(f"response:\n {response}")
print(f"=================================================================================================")

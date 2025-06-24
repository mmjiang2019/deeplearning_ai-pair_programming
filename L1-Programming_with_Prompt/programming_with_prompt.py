from pair_programming.utils import open_ai

chat = open_ai.NewOpenAIClient()

# select a model here
models = open_ai.select_model(client=chat, prefixes=["gemma"])
print(f"models: \n{models}")
model = models[0].id
print(f"selected: \n{model}")

print(f"selected model: {model}")
prompt = "Show me how to iterate across a list in Python."
print(f"prompt: \n{prompt}")
response = open_ai.get_completion(client=chat, model=model, prompt=prompt)
print(f"response: \n{response}")
print(f"=================================================================================================")

prompt = "write code to iterate across a list in Python"
print(f"prompt: \n{prompt}")
response = open_ai.get_completion(client=chat, model=model, prompt=prompt)
print(f"response: \n{response}")
print(f"=================================================================================================")

prompt = "how to realize parallelism using python"
print(f"prompt: \n{prompt}")
response = open_ai.get_completion(client=chat, model=model, prompt=prompt)
print(f"response: \n{response}")
print(f"=================================================================================================")

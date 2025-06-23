from pair_programming.utils import open_ai


model = "deepseek-coder:1.3b"

chat = open_ai.NewOpenAIClient()
for m in open_ai.list_models(client=chat):
    print(f"model id: {m.id}")

models = [m for m in open_ai.list_models(client=chat) if "coder" in m.id and "deepseek" in m.id]
print(f"models: \n{models}")

prompt = "Show me how to iterate across a list in Python."
response = open_ai.get_completion(client=chat, model=model, prompt=prompt)
print(f"response: \n{response}")
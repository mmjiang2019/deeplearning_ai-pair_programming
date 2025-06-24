from pair_programming.utils import open_ai

chat = open_ai.NewOpenAIClient()

# select a model here
models = open_ai.select_model(client=chat, prefixes=["gemma"])
print(f"models: \n{models}")
model = models[0].id
print(f"selected: \n{model}")

priming = "You are an expert at writing clear, concise, Python code."
question = """
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

"""

prompt_template = """
{priming}

Can you please make this code more efficient?

{question}

Explain in detail what you changed and why.
"""

prompt = prompt_template.format(priming=priming, question=question)
print(f"prompt:\n {prompt}")
response = open_ai.get_completion(client=chat, prompt=prompt, model=model)
print(f"response:\n {response}")
print(f"=================================================================================================")

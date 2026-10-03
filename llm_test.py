from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-360M-Instruct"
)

messages = [
    {
        "role": "system",
        "content": "Extract the target object from the user's robot instruction. Return only the object name."
    },
    {
        "role": "user",
        "content": "Please move toward the bottle on the left."
    }
]

response = generator(
    messages,
    max_new_tokens=10,
    do_sample=False
)


answer = response[0]["generated_text"][-1]["content"]
print("LLM answer:", answer)


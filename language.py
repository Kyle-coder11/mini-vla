# def extract_target(instruction):
#     instruction = instruction.strip().lower()
#     words = instruction.split()
#     return words[-1]

# text = input("instruction: ")
# target = extract_target(text)
# print("extracted target:", target)

from transformers import pipeline


generator = pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-360M-Instruct"
)


def extract_target(instruction, detected_objects):

    object_list = ", ".join(detected_objects)

    prompt = (
        f"Detected objects: {object_list}\n"
        f"Robot instruction: {instruction}\n\n"
        "Select the detected object that best matches the instruction. "
        "Return only one object name from the detected object list. "
        "Do not explain."
    )

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = generator(
        messages,
        max_new_tokens=10,
        do_sample=False
    )

    target = response[0]["generated_text"][-1]["content"]
    target = target.strip().lower()
    target = target.strip('"\' ')

    return target


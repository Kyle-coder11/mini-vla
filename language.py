def extract_target(instruction):
    instruction = instruction.strip().lower()
    words = instruction.split()
    return words[-1]

# text = input("instruction: ")
# target = extract_target(text)
# print("extracted target:", target)


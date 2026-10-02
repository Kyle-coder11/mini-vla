target = input("what object do u want to find?")
print("you asked for:", target)
detected_object = ["cup", "laptop", "mouse", "person"]

for obj in detected_object:
    if obj == target:
        print("found:", obj)
    else:
        print("target not found!")




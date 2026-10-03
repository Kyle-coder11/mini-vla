# def choose_action(target_x, image_x):
#     image_center_x = image_x / 2
#     tolerance = 50

#     left_boundary = image_center_x - tolerance
#     right_boundary = image_center_x +tolerance
    
#     # if image_center_x + tolerance < target_x :
#     if target_x > right_boundary:
#         return "Turn Right"
#     # elif image_center_x - tolerance > target_x:
#     elif target_x < left_boundary:
#         return "Turn Left"
#     else:
#         return "move forward"
    
# action = choose_action(100, 640)
# print(action)
import torch
from policy_nn import PolicyNetwork

actions = [
    "TURN LEFT",
    "MOVE FORWARD",
    "TURN RIGHT"
]

model = PolicyNetwork()

model.load_state_dict(
    torch.load("policy_model.pt")
)

model.eval()

def choose_action(target_x, image_width):
    normalized_x = target_x / image_width
    x = torch.tensor([[normalized_x]], dtype=torch.float32)
    with torch.no_grad():
        output = model(x)
        predicted_class = torch.argmax(
            output, 
            dim=1
        ).item()

    return actions[predicted_class]

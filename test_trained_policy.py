import torch

from policy_nn import PolicyNetwork


model = PolicyNetwork()

model.load_state_dict(
    torch.load("policy_model.pt")
)

model.eval()


actions = [
    "TURN LEFT",
    "MOVE FORWARD",
    "TURN RIGHT"
]


test_x = torch.tensor(
    [[0.8]],
    dtype=torch.float32
)


with torch.no_grad():

    output = model(test_x)

    predicted_class = torch.argmax(
        output,
        dim=1
    ).item()


print("Network output:", output)
print("Predicted class:", predicted_class)
print("Predicted action:", actions[predicted_class])
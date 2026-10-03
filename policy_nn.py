import torch
import torch.nn as nn
class PolicyNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(1, 16),
            nn.ReLU(),
            nn.Linear(16, 3)
        )

    def forward(self, x):
        return self.network(x)


model = PolicyNetwork()

x = torch.tensor([[0.8]])
output = model(x)
print("Network output:", output)

actions = [
    "TURN LEFT",
    "MOVE FORWARD",
    "TURN RIGHT"
]

predicted_class = torch.argmax(output, dim=1).item()
print("Predicted class:", predicted_class)
print("Predicted action:", actions[predicted_class])
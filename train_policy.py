import torch
import torch.nn as nn
import torch.optim as optim

from policy_nn import PolicyNetwork


# Training inputs
# Each inner list is one example with one feature:
# normalized target x-position
X = torch.tensor([
    [0.10],
    [0.20],
    [0.30],
    [0.45],
    [0.50],
    [0.55],
    [0.70],
    [0.80],
    [0.90]
], dtype=torch.float32)


# Correct action labels
# 0 = TURN LEFT
# 1 = MOVE FORWARD
# 2 = TURN RIGHT
y = torch.tensor([
    0,
    0,
    0,
    1,
    1,
    1,
    2,
    2,
    2
], dtype=torch.long)


model = PolicyNetwork()


loss_function = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.01
)


for epoch in range(500):

    output = model(X)

    loss = loss_function(
        output,
        y
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()


    if epoch % 50 == 0:
        print(
            "Epoch:",
            epoch,
            "Loss:",
            round(loss.item(), 4)
        )


torch.save(
    model.state_dict(),
    "policy_model.pt"
)

print("Model saved!")
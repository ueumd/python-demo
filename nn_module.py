import torch
from torch import nn

# 神经网络模版
class Ueumd(nn.Module):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, input):
        output = input + 1
        return output

# 创建神经网络
ueumd = Ueumd()
x = torch.tensor(1.0)

output = ueumd(x)
print(output)
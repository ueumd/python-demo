import torch

dev = torch.device("cpu")

a= torch.tensor([2,2],
                  dtype=torch.float32,
                  device=dev
                  )
print(a)
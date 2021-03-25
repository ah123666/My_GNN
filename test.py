import torch

A = torch.tensor([
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
], dtype=torch.float32)

D = torch.tensor([
    [2, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0],
    [0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 1],
], dtype=torch.float32)

print('A:\n', A)
# print(D.inverse())
D_minus_inverse = D.inverse().sqrt()
print('D_minus_inverse:\n', D_minus_inverse)
print('D_minus_inverse @ A:\n', D_minus_inverse @ A)
print('D_minus_inverse @ A:\n', D_minus_inverse @ A @ D_minus_inverse)

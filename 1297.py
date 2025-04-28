import math

n = input()

D, H, W = n.split()
D, H, W = int(D), int(H), int(W)

print(math.floor(math.sqrt(D ** 2 / (H ** 2 + W ** 2)) * H), math.floor(math.sqrt(D ** 2 / (H ** 2 + W ** 2)) * W))
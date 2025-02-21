# we are just gonna generate some test cases

import random
import sys

sys.stdout = open("01.in", "w")


N = 100
K = 1000

print(N,K)

for _ in range(N):
    type = random.choice(["NZ", "DIP", "IT"])
    name = _ + 1
    print(type, name)
for _ in range(K):
    print(random.choice(["NZ", "DIP", "IT"]))
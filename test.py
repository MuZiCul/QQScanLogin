import random

sRandomMask = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
sRandomVal = ''
for _ in range(6):
    rIndex = random.randint(0, 61)
    sRandomVal += sRandomMask[rIndex]

print(sRandomVal)

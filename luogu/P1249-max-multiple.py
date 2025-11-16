import math

n = int(input())
m = 1
k = math.floor((math.sqrt(9 + 8 * n) - 1) / 2)

result = list(range(2, k + 1))
l = len(result)

q = n - (k * (k + 1) // 2 - 1)

for i in range(0, q) :
    result[(l - 1) - i % l] += 1

for r in result :
    m *= r

print(" ".join(map(str, result)))
print(m)

# Metadata
# Created: 2026-03-26T09:47:22 (UTC +08:00)
# Source: https://acm.creative3605.com/contest/2036113138187444224/problem/A
# Problem Title: Monster Sequence Game (Alice vs Bob)
#
# Problem Description:
# An impartial game played on a line of n monsters with a parameter K.
# Players take turns with two possible operations:
# 1. Destroy a continuous sequence of size 1 <= L <= K. 
#    - This reduces the sequence but keeps it as one piece.
# 2. Destroy exactly K continuous monsters such that the original sequence 
#    is split into TWO non-empty, independent sequences.
#
# Game Theory Logic:
# - This is a Sprague-Grundy theorem problem.
# - The game state is the length of the monster sequence.
# - Operation 1 on a sequence of size less than k to 0.
# - Operation 2 on a sequence of size N leads to two states (i) and (N - K - i) 
#   where i > 0 and (N - K - i) > 0.
# - The Grundy value (SG value) of a split state is: SG(i) ^ SG(N - K - i).
# - Alice wins if the initial SG(n) != 0.
#
# Guarantee 1 <= T <= 10000, 2 <= K <= 10 ** 7, 0 <= n <= 10 ** 9
#
# Constraints:
# - Likely solved via DP to precalculate SG values up to n.

N = 1000005
f = [-1] * N

def sg(x: int, k: int) -> int :
    if f[x] != -1 :
        return f[x]
    s = set()
    """s is prepared for mex operation, which stores the states of successors"""

    if x <= k and x > 0 :
        s.add(sg(0, k))
    else :
        for i in range(1, x - k) :
            s.add(sg(i, k) ^ sg(x - k - i, k))

    i = 0
    while True :
        if i not in s :
            f[x] = i
            return i
        i += 1

def precompute() -> None :
    k = 8
    for i in range(1, 101) :
        print(sg(i, k), end=" ")
        if (i % (4 * k + 2) == 0) :
            print("\n", end="")

def solve() :
    t = int(input().rstrip())
    for _ in range(t) :
        k, n = map(int, input().rstrip().split())
        if n % (4 * k + 2) == k + 1 :
            print("Bob")
        else :
            print("Alice")

if __name__ == "__main__" :
    p = False

    if p :
        precompute()
    else :
        solve()
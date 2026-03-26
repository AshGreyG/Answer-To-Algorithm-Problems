# Metadata
# Created: 2026-03-26T11:05:02 (UTC +08:00)
# Source: https://www.luogu.com.cn/problem/P2197
# Problem Title: [Template] Nim Game (Nim 游戏模板)
#
# Problem Description:
# Two players, A and B, play a game with 'n' piles of stones. 
# In each turn, a player chooses one pile and removes any number 
# of stones (at least one). The last player to move wins (Normal Play Convention).
#
# Mathematical Logic (Bouton's Theorem):
# - Let the sizes of the piles be a1, a2, ..., an.
# - The Nim-sum is defined as: S = a1 ⊕ a2 ⊕ ... ⊕ an (where ⊕ is XOR).
# - If S == 0: The current state is a P-position (Previous player winning).
#   The first player (A) will lose if the second player (B) plays optimally.
# - If S != 0: The current state is an N-position (Next player winning).
#   The first player (A) has a winning strategy.
#
# Complexity:
# - Time: O(n) per test case to calculate the XOR sum.
# - Space: O(1) beyond storing input.
#
# Input/Output:
# - For each case, output 'Yes' if the first player wins, otherwise 'No'.

def main() -> None :
    t = int(input().rstrip())
    """The number of data groups"""
    results = []

    for _ in range(t) :
        n = int(input().rstrip())
        """The number of stone heaps"""
        heaps = list(map(int, input().rstrip().split()))
        """Stone heaps"""

        sg = heaps[0]
        """Sprague-Grundy sum of nim game, or nim sum or Bouton sum"""
        for i in range(1, len(heaps)) :
            sg ^= heaps[i]

        results.append(sg)

    for s in results :
        if s == 0 :
            print("No")
        else :
            print("Yes")

if __name__ == "__main__" :
    main()
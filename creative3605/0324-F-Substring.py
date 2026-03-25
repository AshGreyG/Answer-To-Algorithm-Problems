# Metadata
# Created: 2026-03-24T17:08:37 (UTC +08:00)
# Source: https://acm.creative3605.com/competition/2036113138187444224/problem/F
# Problem Title: Maximum Palindrome Score (Single Character Type)
#
# Problem Description:
# Given a string S of length n, select K disjoint palindromic substrings 
# s_1, s_2, ..., s_k such that each substring contains at most ONE 
# kind of letter (e.g., "aaa", "bb", "c").
#
# Goal:
# Maximize the score defined as: Σ(len(s_i)) - K.
#
# Logic Insight:
# - A palindrome consisting of only one type of character is simply a 
#   contiguous block of identical characters.
# - The score contribution of a single block of length L is (L - 1).
# - Since we want to maximize the total length while minimizing the number 
#   of substrings (K), the optimal strategy is to pick the longest possible 
#   contiguous blocks of identical characters.
# - Total Maximum Score = Σ (length of each maximal contiguous block - 1).
#
# Complexity:
# - Time: O(n) - Single pass through the string.
# - Space: O(1) - Only requires pointers/counters.

def main() -> None :
    t = int(input().rstrip())
    results = []

    for _ in range(t) :
        s = input().rstrip()
        score = 0
        for i in range(len(s) - 1) :
            if s[i] == s[i + 1] :
                score += 1
        results.append(score)

    for r in results :
        print(r)

if __name__ == "__main__" :
    main()
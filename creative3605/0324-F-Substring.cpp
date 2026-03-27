// Metadata
// Created: 2026-03-24T17:08:37 (UTC +08:00)
// Source: https://acm.creative3605.com/competition/2036113138187444224/problem/F
// Problem Title: Maximum Palindrome Score (Single Character Type)
//
// Problem Description:
// Given a string S of length n, select K disjoint palindromic substrings 
// s_1, s_2, ..., s_k such that each substring contains at most ONE 
// kind of letter (e.g., "aaa", "bb", "c").
//
// Goal:
// Maximize the score defined as: Σ(len(s_i)) - K.
//
// Logic Insight:
// - A palindrome consisting of only one type of character is simply a 
//   contiguous block of identical characters.
// - The score contribution of a single block of length L is (L - 1).
// - Since we want to maximize the total length while minimizing the number 
//   of substrings (K), the optimal strategy is to pick the longest possible 
//   contiguous blocks of identical characters.
// - Total Maximum Score = Σ (length of each maximal contiguous block - 1).
//
// Complexity:
// - Time: O(n) - Single pass through the string.
// - Space: O(1) - Only requires pointers/counters.

#include <iostream>
#include <vector>
#include <string>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0), std::cout.tie(0);

    int t;
    std::cin >> t;
    std::vector<int> results;

    for (int i = 0; i < t; ++i) {
        std::string s;
        std::cin >> s;
        int score = 0;
        for (int j = 0; j < s.size() - 1; ++j) {
            if (s[j] == s[j + 1]) score++;
        }
        results.push_back(score);
    }

    for (const auto &r : results) std::cout << r << "\n";

    return 0;
}
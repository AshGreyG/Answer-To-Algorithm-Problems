// Metadata
// Created: 2026-03-26T09:47:22 (UTC +08:00)
// Source: https://acm.creative3605.com/contest/2036113138187444224/problem/A
// Problem Title: Monster Sequence Game (Alice vs Bob)
//
// Problem Description:
// An impartial game played on a line of n monsters with a parameter K.
// Players take turns with two possible operations:
// 1. Destroy a continuous sequence of size 1 <= L <= K. 
//    - This reduces the sequence but keeps it as one piece.
// 2. Destroy exactly K continuous monsters such that the original sequence 
//    is split into TWO non-empty, independent sequences.
//
// Game Theory Logic:
// - This is a Sprague-Grundy theorem problem.
// - The game state is the length of the monster sequence.
// - Operation 1 on a sequence of size less than k to 0.
// - Operation 2 on a sequence of size N leads to two states (i) and (N - K - i) 
//   where i > 0 and (N - K - i) > 0.
// - The Grundy value (SG value) of a split state is: SG(i) ^ SG(N - K - i).
// - Alice wins if the initial SG(n) != 0.
//
// Guarantee 1 <= T <= 10000, 2 <= K <= 10 ** 7, 0 <= n <= 10 ** 9
//
// Constraints:
// - Likely solved via DP to precalculate SG values up to n.

#include <cstring>
#include <iostream>
#include <set>

typedef long long LL;
const int N = 1e6 + 5;
LL f[N];

int sg(int x, int k) {
    if (f[x] != -1) return f[x]; // reduce duplicate calculation
    std::set<int> S;

    if (x <= k && x > 0) {
        S.insert(sg(0, k));
        // here x stands for the length of monster sequence, when 0 < x <= k,
        // the first player can removes all of them, actually the sg(0, k) must
        // be 0
    } else {
        for (int i = 1; i <= x - k - 1; ++i) {
            S.insert(sg(i, k) ^ sg(x - k - i, k));
        }
        // Actually only when x >= k + 1, this for loop can be executed.
        // [ ] [ ] [ ] [ ] [ ] [ ]  [ ] [ ] [ ]
        //      ↑           ↑
        // Assume that k = 4, and now i stands for the length of one part
    }

    for (int i = 0;; ++i) {
        if (S.count(i) == 0) {
            f[x] = i;
            return i;
        }
    }
    // This is the mex part
}

void precompute() {
    int k = 4;
    for (int i = 1; i <= 100; ++i) {
        std::memset(f, -1, sizeof(f));
        std::cout << sg(i, k) << " ";
        if (i % (4 * k + 2) == 0) std::cout << "\n";
    }
}

void solve() {
    int t;
    std::cin >> t;

    for (int i = 0; i < t; ++i) {
        int k, n;
        std::cin >> k >> n;
        if (n % (4 * k + 2) == k + 1) {
            std::cout << "Bob\n";
        } else {
            std::cout << "Alice\n";
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0), std::cout.tie(0);

    bool p = false;
    if (p) precompute(); else solve();
    return 0;
}
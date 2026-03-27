# Metadata
# Created: 2026-03-27T13:15:28 (UTC +08:00)
# Source: https://acm.creative3605.com/contest/2036113138187444224/problem/B
# Problem Title: Maximum Binary Number after K Flips
#
# Problem Description:
# Given a binary string of length n and an operation count k. 
# One operation consists of flipping all bits in an interval [l, r].
# Find the lexicographically largest binary string possible after 
# exactly k operations.
#
# Greedy Strategy:
# 1. To maximize a binary number, we want the prefix to have as many 1s 
#    as possible.
# 2. Identify contiguous blocks of 0s. Each such block can be turned 
#    into 1s using a single operation.
# 3. If k is less than the number of 0-blocks, flip the first k blocks.
# 4. If k is greater than or equal to the number of 0-blocks:
#    - All 0s can be turned into 1s.
#    - If the remaining operations (k - used) are even, the string 
#      stays all 1s.
#    - If the remaining operations are odd, we must perform one extra flip. 
#      To keep the number "largest," we flip the least significant bit (s_n).
#      Note: The problem says "exactly k times." However, we can usually 
#      flip an interval and flip it back to use 2 operations.
#
# Constraints:
# - T <= 6e4, Sum of n <= 2.5e6.
# - k can be very large (up to 10^18), so use O(n) per test case.

def main(debug: bool = False) -> None :
    t = int(input().rstrip())
    results = []

    for _ in range(t) :
        n, k = map(int, input().rstrip().split())
        s = input().rstrip()
        muts = list(s)
        """Mutable version of s"""
        zeros = [index for index, char in enumerate(s) if char == "0"]
        """Stores the index of all zeros in input"""
        chunk_starts = []
        """Stores the beginning index of continuous zeros in input"""

        if len(s) == 1 and k % 2 == 0 :
            results.append("1")
            continue
        elif len(s) == 1 and k % 2 == 1 :
            results.append("0")
            continue

        if len(zeros) == 0 and k != 1 :
            results.append(s)
            continue
        elif len(zeros) == 0 and k == 1 :
            # It's the most special case: there is no zero chunk and we must
            # flip 1 time, we can only flip the lowest digit.
            results.append(s[:len(s) - 1] + "0")
            continue

        # Only when there are continuous zero chunks in input
        chunk_starts.append(zeros[0])
        for i in range(len(zeros) - 1) :
            if zeros[i + 1] - zeros[i] != 1 :
                chunk_starts.append(zeros[i + 1])

        if debug :
            print(f"Processing {s}, its chunk starting index is {chunk_starts}")
            print(f"Processing {s}, its zeros chunk index is {zeros}")

        flip = k - (len(chunk_starts) - 1)
        if flip <= 0 :
            # There is no enough operation to flip all continuous zero chunks
            count = 0
            """Counts the flip chunk operations"""
            for start in chunk_starts :
                if count >= k :
                    break
                else :
                    count += 1

                i = start
                while True :
                    if i > len(s) - 1 :
                        break

                    muts[i] = "1"
                    if debug :
                        print(f"Processing {s}, changing 0 of index {i}")

                    if i > len(s) - 2 :
                        break
                    if s[i + 1] != s[i] :
                        # Python doesn't have do...while keyword, so we need
                        # to use `while True...if break` to do so.
                        break
                    else :
                        i += 1
        else :
            # There are enough operations to flip all continuous zero chunks, and
            # left even numbers of operations to invert the last zero chunk (
            # from 0 -> 1 -> 0 -> 1, inverted to 1). So actually the flipped
            # s is "111...11"
            for i in range(len(muts)) :
                muts[i] = "1"

        results.append("".join(muts))

    for r in results :
        print(r)

if __name__ == "__main__" :
    main(debug=True)

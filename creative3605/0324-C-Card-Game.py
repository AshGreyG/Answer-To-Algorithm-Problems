# Metadata
# Created: 2026-03-27T21:35:19 (UTC +08:00)
# Source: https://acm.creative3605.com/problem/2036107112063115264
# Problem Title: Maximum Cards Moveable (Tower of Hanoi Variation)
#
# Problem Description:
# Given n piles. One pile contains k cards in decreasing consecutive order 
# (k, k-1, ..., 1). Other piles are empty.
# Find the maximum k such that all k cards can be moved to another 
# specific empty pile without violating the "decreasing and consecutive" 
# stacking rule.
#
# Mathematical Insight:
# - This is a variation of the revealable/movable stack problem.
# - For n piles, the maximum number of cards k that can be moved 
#   following these rules is 2^(n-1) - 1.
# - Logic: To move a stack to pile 2, you can use the other n-2 piles 
#   as intermediate buffers. Each additional pile doubles the capacity 
#   because you can move a full valid stack to a buffer, then move 
#   another stack to the destination, then move the buffer stack back.
#
# Constraints:
# - Result should be taken modulo 998244353.
# - Since n can be large, use modular exponentiation pow(2, n-1) - 1 mod 998244353.
#
# Edge Case:
# - If n < 2, k = 0 (cannot move to "another" pile).
# - If n = 2, k = 2^(2-1) - 1 = 1.

# We could first think about when n = 3, maximum of k is 3
# 3, 2, 1         (pile 1)
#                 (pile 2)
#                 (pile 3)

# 3, 2            (pile 1)
# 1               (pile 2)
#                 (pile 3)

# 3               (pile 1)
# 1               (pile 2)
# 2               (pile 3)

# 3               (pile 1)
#                 (pile 2)
# 2 1             (pile 3)

#                 (pile 1)
# 3               (pile 2)
# 2 1             (pile 3)

# 1               (pile 1)
# 3               (pile 2)
# 2               (pile 3)

# 1               (pile 1)
# 3 2             (pile 2)
#                 (pile 3)

#                 (pile 1)
# 3 2 1           (pile 2)
#                 (pile 3)

import collections
import sys
sys.setrecursionlimit(10000)

def is_solvable(n: int, k: int, debug: bool = False) -> bool :
    """ This function checks whether a game of n piles, k cards can be solved.
    It uses BFS algorithm to exhaustively search the way from source to target.
    """

    if k == 0 :
        return True
    # initial pile 0 has (1, k), others are empty
    initial = [(1, k) if i == 0 else None for i in range(n)]
    goal    = [(1, k) if i == 1 else None for i in range(n)]

    def state_to_tuple(state) :
        return tuple(None if p is None else (p[0], p[1]) for p in state)

    def tuple_to_state(tuples) :
        return [None if p is None else [p[0], p[1]] for p in tuples]

    start  = state_to_tuple(initial)
    goal_t = state_to_tuple(goal)

    if start == goal_t :
        # when our initial state equals to our target, it's solvable
        return True

    visited = set()
    """
    Stores every visited state of n piles, it stores tuple of every state of
    n piles
    """
    queue = collections.deque([start])
    """
    Stores every movable state of n piles, when the state cannot move anymore, it will
    be dropped by `popleft` method and will never be processed tp a new state and be added
    to this queue. So only when queue is empty and in the exhaustive searching there is
    no state matching our goal, we should return False.
    """
    visited.add(start)

    while queue :
        current_tuple = queue.popleft()
        if current_tuple == goal_t :
            return True
        if debug :
            print(f"Now processing {current_tuple}")
        # reconstruct current as list of [min, max] or None
        current = tuple_to_state(current_tuple)

        for i in range(n) :
            if current[i] is None :
                continue
            top = current[i][0]
            # top element of current processing pile
            bottom = current[i][1]
            # bottom element of current processing pile
            for j in range(n) :
                if i == j :
                    # skip same pile
                    continue
                # try to move
                # first copy the current (notice we cannot use .copy method
                # because there are lists in current, .copy method is a shallow
                # copy)
                new = [None if lst is None else lst[:] for lst in current]
                # remove top from pile i
                if top == bottom :
                    new[i] = None
                else :
                    new[i] = [top + 1, bottom]
                # add this top to pile j
                can_move = False
                if new[j] is None :
                    new[j] = [top, top]
                    can_move = True
                else :
                    target_top = new[j][0]
                    if target_top == top + 1 :
                        new[j][0] = top
                        can_move = True
                if not can_move :
                    # when we cannot move the top, we should skip adding new
                    # state to the visited set
                    continue
                new_tuple = state_to_tuple(new)
                if new_tuple not in visited :
                    if debug :
                        print(f"  → After processing, new state is {new_tuple}")
                    visited.add(new_tuple)
                    queue.append(new_tuple)
    return False

def precompute() -> None :
    results = {}
    for n in range(2, 6) :
        max_k = 0
        for k in range(1, 200) :
            if is_solvable(n, k) :
                max_k = k
            else :
                break
        results[n] = max_k

    for n in results.keys() :
        print(f"When we have {n} piles, the maximum number of cards is {results[n]}")

def solve() -> None :
    t = int(input().rstrip())
    results = []
    for _ in range(t) :
        n = int(input().rstrip())
        k = pow(2, n - 1, 998244353) - 1
        results.append(k)

    for k in results :
        print(k)

def main() -> None :
    # We can think of the card number k as a function of pile number n: k = f[n]
    # Move the top card from the initial pile stack to an empty pile, this pile
    # cannot place any card onto it
    p = True
    if p :
        precompute()
        # When we have 2 piles, the maximum number of cards is 1
        # When we have 3 piles, the maximum number of cards is 3
        # When we have 4 piles, the maximum number of cards is 7
        # When we have 5 piles, the maximum number of cards is 15
        # 
        # f(n) = 2 * f(n - 1) + 1
        # 
        # thus f(n) = 2^(n-1) - 1
    else :
        solve()

if __name__ == "__main__" :
    main()
# Metadata
# Created: 2026-03-21T20:11:34 (UTC +08:00)
# Source: http://123.60.95.133/contest/2/problem/A0006
# Problem Title: Chujun Loves Fishing (储君爱钓鱼)
#
# Problem Description:
# A fisherman has 'h' hours to fish across 'n' ponds arranged in a line.
# - Travel time between pond i and i+1 is t[i] (it's not in 5-min units).
# - Initial fish yield at pond i is F[i] per 5-minute unit.
# - Yield decreases by d[i] after every 5-minute unit spent at that pond.
# - Total time must be a multiple of 5 minutes.
# 
# Task:
# Find the maximum total fish caught across all possible pond-visiting 
# strategies and time allocations.
#
# Constraints:
# - 1 <= h <= 16 (Total hours)
# - 2 <= n <= 25 (Number of ponds)
# - 0 <= Fi, di <= 100
# - 1 unit of time = 5 minutes.
#
# Logic Hint: 
# Since n is small, you can enumerate the furthest pond 'k' reached. 
# Subtract the fixed travel time to reach 'k', then greedily pick the 
# pond with the current highest yield among ponds 1 to 'k' for the 
# remaining time.

import heapq

UNIT_TIME = 5

def main(debug: bool = False) -> None :
    n = int(input().rstrip())
    """The number of ponds 2 <= n <= 25"""
    h = int(input().rstrip()) * 60
    """The number of total fishing hours (we convert to minutes), 1 <= h <= 16"""
    f = list(map(int, input().rstrip().split()))
    """The initial yielded fish at pond i"""
    d = list(map(int, input().rstrip().split()))
    """The decreasing fish at pond i after an unit time"""
    t = list(map(int, input().rstrip().split()))
    """The consuming time between pond i-1 and pond i"""

    max_fish = 0

    for k in range(1, n + 1) :
        travel_time = sum(t[:k - 1])
        # Calculate the travel time to reach pond k (0-indexed, so up to k - 1)
        remaining_time = h - travel_time
        remaining_unit = remaining_time // UNIT_TIME

        if remaining_time <= 0 :
            break

        current_fish = 0
        # Use a max-priority queue to always pick the pond with most fish. Store
        # as (-yield, decay, index). Python implements heapq as a min-priority queue.
        pq = []
        for i in range(k) :
            heapq.heappush(pq, (-f[i], d[i], i))

        temp_unit = remaining_unit
        while temp_unit > 0 and pq :
            current_yield, decay, index = heapq.heappop(pq)
            current_yield = -current_yield
            current_fish += current_yield
            new_yield = current_yield - decay

            if new_yield > 0 :
                heapq.heappush(pq, (-new_yield, decay, index))
            if debug :
                print("Destination Pond [{:<2}] | index [{:>2}] | current_yield [{:>2}] | current_fish [{:>2}]".format(
                    k,
                    index + 1,
                    current_yield,
                    current_fish
                ))

            temp_unit -= 1

        max_fish = max(max_fish, current_fish)

    print(max_fish)

if __name__ == "__main__" :
    main()
# Metadata
# Created: 2026-03-23T17:07:39 (UTC +08:00)
# Source: https://acm.creative3605.com/problem/916
# Problem Title: BIT Subway Promotion (Beijing International Transport)
#
# Problem Description:
# Comparison between two billing methods for subway tickets based on monthly spending:
# - Discount Tiers: 
#   - Total spent < 100: No discount.
#   - 100 <= Total spent < 200: 20% off (pay 0.8y).
#   - Total spent >= 200: 50% off (pay 0.5y).
#
# Two Calculation Methods:
# 1. DLee's Thought (Continuous): A single ticket can be split. If a 10 CNY ticket
#    is bought when total spent is 99, the first 1 CNY is full price to reach 100, 
#    and the remaining 9 CNY is discounted at 0.8.
# 2. Real Method (Discrete): The discount only applies to the NEXT ticket 
#    purchased after the threshold is met or exceeded.
#
# Task:
# For each month, calculate the total cost under both methods given n tickets.
#
# Constraints:
# - T <= 10 (Test cases/months)
# - n <= 10^5 (Tickets per month)
# - a_i <= 200 (Price per ticket)
#
# Output:
# Two numbers with three decimal places: [DLee's Cost] [Real Cost]

def main(debug: bool = False) -> None :
    t = int(input().rstrip())
    for _ in range(t) :
        a = int(input().rstrip())
        tickets = list(map(int, input().rstrip().split()))
        sum1 = 0
        sum2 = 0
        has_greater1_100 = False
        has_greater1_200 = False
        has_greater2_100 = False
        has_greater2_200 = False

        for tk in tickets :
            if debug :
                print(f"sum1={sum1}")

            temp_sum1 = sum1
            temp_sum1 += tk
            if temp_sum1 <= 100 :
                sum1 += tk
            elif temp_sum1 > 100 and not has_greater1_100 :
                remaining = tk - (100 - sum1)
                # for example, when sum1 is $98, we want the ticket price ($7)
                # to transfer $2 to make sum1 to achieve $100, so `100 - sum1`
                # is the transferred price. And `tk - (100 - sum1)` is the
                # remaining price that will be taken into discount, which is
                # multiplied with discount percent 80%.

                sum1 = 100 + remaining * 0.8
                # so sum1 should be re-assigned to $100 with the remaining price
                # taken into discount (discount percent is 80%).

                has_greater1_100 = True
            elif temp_sum1 >= 100 and temp_sum1 < 200 :
                sum1 += tk * 0.8
            elif temp_sum1 > 200 and not has_greater1_200 :
                remaining = tk - (200 - sum1) / 0.8
                # for example, when sum1 is $198, we want the ticket price ($7)
                # to transfer $2.5 (discount percent 80%) to make sum1 to achieve
                # $100, so `(200 - sum1) / 0.8` is the transferred price.
                # And `tk - (200 - sum1) / 0.8` is the remaining price that will
                # be taken into discount, which is multiplied with discount
                # percent 50%.

                sum1 = 200 + remaining * 0.5
                # so sum1 should be re-assigned to $200 with the remaining price
                # taken into discount (discount percent is 50%).

                has_greater1_200 = True
            else :
                sum1 += tk * 0.5

            if sum2 < 100 :
                sum2 += tk
            elif sum2 >= 100 and sum2 < 200 :
                sum2 += tk * 0.8
            else :
                sum2 += tk * 0.5

        print("{:.3f} {:.3f}".format(sum1, sum2))

if __name__ == "__main__" :
    main(debug=False)
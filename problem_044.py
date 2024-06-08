"""
Pentagonal numbers are generated by the formula, P_n = n(3n - 1)/2.
The first ten pentagonal numbers are: 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P_4 + P_7 = P_8. However, their difference is not pentagonal.

Find the pair of pentagonal numbers, P_j and P_k,
for which their sum and difference are pentagonal and D = |P_k - P_j| is minimised; what is the value of D?
"""

upper_limit = 2170

# P_n = 3/2 n**2 - 1/2 n
# 3 n**2 - n - 2 P_n = 0
# n = (1 +/- sqrt{1 + 4*3*2*P_n})/6

def solution(pen_num: int):

    n = (1 + (1 + 24*pen_num)**0.5) / 6
    
    return n == int(n)

pen_nums = [int(x*(3*x - 1)/2) for x in range(1, upper_limit)]

answer = float("inf")

for i in range(len(pen_nums)):
    for j in range(i + 1, len(pen_nums)):
        if solution(abs(pen_nums[i] - pen_nums[j])) and solution(pen_nums[i] + pen_nums[j]):
            answer = min(answer, pen_nums[j] - pen_nums[i])

print(answer)
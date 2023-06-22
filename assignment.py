def solution(n):
    dp_ways = [1, 2, 4, 8] + [0] * (n - 3)          # Number of ways to attend on nth day
    dp_miss = [0, 1, 2, 4] + [0] * (n - 3)          # Missing graduation on nth day

    for i in range(4, n + 1):
        dp_ways[i] = dp_ways[i - 1] + dp_ways[i - 2] + dp_ways[i - 3] + dp_ways[i - 4]
        dp_miss[i] = dp_miss[i - 1] + dp_miss[i - 2] + dp_miss[i - 3] + dp_miss[i - 4]

    return str(dp_miss[n]) + "/" + str(dp_ways[n])


test_nums = [5, 10]
for n in test_nums:
    res = solution(n)
    print(res)

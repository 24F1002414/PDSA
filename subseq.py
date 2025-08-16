def countSubseq(s):
    n = len(s)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if s[j] < s[i]:
                dp[i] += dp[j]
    return sum(dp)
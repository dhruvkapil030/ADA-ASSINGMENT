
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]


def knapsack(W, wt, val, n):
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w]=0
            elif wt[i-1] <= w:
                dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][W]


def matrix_chain(p):
    n = len(p)
    dp = [[0]*n for _ in range(n)]
    for l in range(2,n):
        for i in range(1,n-l+1):
            j = i+l-1
            dp[i][j] = float('inf')
            for k in range(i,j):
                q = dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j]
                dp[i][j] = min(dp[i][j], q)
    return dp[1][n-1]

print("LCS:", lcs("ABCBDAB","BDCAB"))

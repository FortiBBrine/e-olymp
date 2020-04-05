n = int(input())
num = list(map(int, input().split()))
nek1, nek2 = [], []
ans = []
if n%2 == 0:
    ans = [0] * n
    for i in range(0, n//2): ans[i*2] = num[i]
    j = 1
    for i in range(n//2, n):
        ans[j] = num[i] 
        j+=2
elif n%2:
    ans = [0] * n
    for i in range(0, (n+1)//2): ans[i*2] = num[i]
    j = 1
    for i in range((n+1)//2, n):
        ans[j] = num[i] 
        j+=2
print(*ans, sep = ' ')
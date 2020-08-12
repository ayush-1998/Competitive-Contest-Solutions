def fun(raw):
    arr = []
    for i in range(len(raw)):
        arr.append((raw[i][0], raw[i][1], i))
    arr.sort()
    c = 0
    j = 0
    res = []
    for start, end, idx in arr:
        if start < c and start < j:
            return "IMPOSSIBLE"
        if start >= c:
            res.append(('C', idx))
            c = end
        else:
            res.append(('J', idx))
            j = end
    ans = ''
    for a, idx in sorted(res, key=lambda x: x[1]):
        ans += a
    return ans
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        interval = [int(s) for s in input().split(" ")]
        arr.append(interval)
    ans = fun(arr)
    print("Case #{}: {}".format(t, ans))


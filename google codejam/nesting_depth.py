def fun(t,ans,pre):
    if pre != '' and t != '':
        if int(pre) > int(t[0]):
            for i in range(int(pre)-int(t[0])):
                ans = ans + ')'
    if t == '':
        for i in range(int(pre)):
            ans = ans + ')'
        return ans
    if int(t[0]) == 0:
        return fun(t[1:],ans + t[0],t[0])
    if int(t[0]) == 1:
        if pre != '':
            if int(pre) == 0:
                ans = ans + '(' + t[0]
            else:
                ans = ans + t[0]
        else:
            ans = ans + '(' + t[0]
        return fun(t[1:],ans,t[0])
    if int(t[0]) > 1:
        if pre != '':
            for i in range(int(t[0]) - int(pre)):
                ans = ans + '('
            ans = ans + t[0]
        else:
            for i in range(int(t[0])):
                ans = ans + '('
            ans = ans + t[0]
        return fun(t[1:],ans,t[0])
t = int(input())
for m in range(0,t):
    k = input()
    print('Case #{}: {}'.format(m + 1,fun(k,'','')))
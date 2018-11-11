a = input().lower().split()
ans = {}
for i in a:
    ans[i] = a.count(i)
for i in ans:
    print(i +" "+str(ans[i]))
s = input()
cnt = 1
t = ""
if len(s) == 1:
    print(s[0] + str(cnt))
else:
    for i in range(len(s)-1):
        out = s[i] + str(cnt)
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            t += out
            cnt = 1
    print(t + s[i+1] + str(cnt)) 
n = int(input())
x_0 = 0
y_0 = 0
cond = []
for i in range(n):
    cond.append(input().split())
for j in range(len(cond)):
    if cond[j][0] == "север":
        y_0 += int(cond[j][1])
    elif cond[j][0] == "юг":
        y_0 -= int(cond[j][1])
    elif cond[j][0] == "запад":
        x_0 -= int(cond[j][1])
    elif cond[j][0] == "восток":
        x_0 += int(cond[j][1])
print(str(x_0)+" "+str(y_0))
# put your python code here
b = []
c = []
while True:
    a = [i for i in input().split()]
    if a == ["end"]:
        break
    else:
        b.append(a)
c = [[0 for i in range(len(b[0]))] for j in range(len(b))]
for i in range(len(b)):
    for j in range(len(b[i])):
        c[i][j] = int(b[i-1][j]) + int(b[i+1-len(b)][j]) + int(b[i][j-1]) + int(b[i][j+1-len(b[0])])
        print(c[i][j], end = " ")
    print()
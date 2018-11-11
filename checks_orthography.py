words_in_voc = int(input())
voc = []
text = []
text_set = set()
for i in range(words_in_voc):
    voc.append(str(input()))

l = int(input())
for j in range(l):
    text += input().split()
    
    
s = set()
for k in text:
    text_set.add(k.lower())
    for m in voc:
        if k.lower() == m.lower():
            s.add(k.lower())
ans = text_set - s
for p in ans:
    print(p)
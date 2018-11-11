alphabet = input()
code = input()
to_code = input()
to_decode = input()

dict_code = {}
for i in range(len(alphabet)):
    dict_code[alphabet[i]] = code[i]
    
dict_decode = {}
for i in range(len(alphabet)):
    dict_decode[code[i]] = alphabet[i]

for j in to_code:
    if j in dict_code:
        print(dict_code[j], end = "")
print()
for j in to_decode:
    if j in dict_decode:
        print(dict_decode[j], end = "")
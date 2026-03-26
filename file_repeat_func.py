print("friends forever")
a=2
b=5
c=a**b
d = a+b
e = a-b
print('a**b=',c)
print(d)
print(e)

strt="The3 qu1ck br0wn f0x jumps 0ver 13 lazy d0gs"
stry=" The3 qu1ck br0wn f0x jumps 0ver 13 lazy d0gs"
sky = ""
for char in stry:
    if char not in sky:
        sky += char
print("without repetition:",sky)
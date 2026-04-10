n = k = 12121
g = 0
if n>0:
  while k>0:
    t= k%10  #gets last number
    g= g*10 + t  # adds number
    k = k//10   # removes last number
print(g)
if n==g:
    print("pallindrome")
else:
    print("Not pallindrome")


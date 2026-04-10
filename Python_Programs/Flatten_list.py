def flatten_list(U):
    res=[]
    for n in U:
        if isinstance(n,list):
            res.extend(n)
        else:
            res.append(n)
    return res
U=(1,2,[4,5],7,8)
print(flatten_list(U))

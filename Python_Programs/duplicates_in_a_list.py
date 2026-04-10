from django.urls import reverse


def duplicates(lst):
    seen=set()
    res=[]
    for items in lst:
        if items not in seen:
            seen.add(items)
            res.append(items)
    return res
lst=(1,11,8,3,4,6,4,7,4,8,9)
P=duplicates(lst)
k=sorted(P,reverse=True)
print(k)
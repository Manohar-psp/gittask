from six import moves


def move_allzeros(lst):
    nonzeros=[]
    zeros=[]
    for n in lst:
        if n==0:
            zeros.append(n)
        else:
            nonzeros.append(n)
    return nonzeros+zeros
lst=(0,1,2,0,4,5,0,6,0,7)
print(move_allzeros(lst))

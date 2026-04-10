def second_l(O):
    largest=max(O)
    second=None
    for n in O:
        if n!=largest:
            if second is None or n>second:
                second=n
    return second
O=(1,4,7,99,56,78,45)
print(second_l(O))

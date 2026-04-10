def pyramid(n):
    for i in range(1,n+1):

        #spaces
        for s in range(n - i):
            print(" ",end="")
        #increasing
        for j in range(1,i+1):
            print(j,end="")
        #decreasing
        for k in range(i-1,0,-1):
            print(k,end="")
        print()
    for i in range(n, 0,-1):

        # spaces
        for s in range(n - i):
            print(" ", end="")
        # increasing
        for j in range(1, i + 1):
            print(j, end="")
        # decreasing
        for k in range(i - 1, 0, -1):
            print(k, end="")
        print()


pyramid(n=4)
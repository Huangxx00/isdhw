for i in range(1,10):
        print(" "*7*i,end="")
        for j in range(i,10):
            a=str.format("{0:1}*{1:1}={2:<3}",i,j,i*j)
            print(a,end="")
        print()

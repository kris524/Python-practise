def staircase(n):
    total_staits = "#"*n
    i = 1
    k = n-1
    while i <= n:
        print(" "*k + "#"*i )
        i+=1
        k-=1
        
staircase(4)
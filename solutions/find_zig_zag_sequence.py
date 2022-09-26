def findZigZagSequence(a, n):
    a.sort() #[1,2,3,4,5]  n = 5 => k = 3 so the first 3 elements are increasing and all after that are decreasing
    mid = int((n + 1)/2)-1 # = 2
    a[mid], a[n-1] = a[n-1], a[mid]  # 4 = 5 5 = 4  [1,2,3,4,5] -> [1,2,5,4,3]

    # st = mid - 1 #1
    st = mid +1
    ed = n - 2 # 4
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st] 
        st = st + 1
        ed = ed - 1
        # print(a)
        #1) 1v4 [1,3,5,4,2]   [3,2,5,4,1]
        #2) 2v3               [3,4,5,2,1]

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')

    return
def isValidSubsequence(array, sequence):
    # Write your code here.
    comparing_array = []
    for i in array:
        if i in sequence:
            if len(comparing_array) == len(sequence):
                break
            comparing_array.append(i)

    print(comparing_array)

    return comparing_array == sequence

        


# print(isValidSubsequence([1,1,1,1], [1,1,1]))
# print([1,2,3]==[1,3,2])

def countingSort(arr):
    max_number = max(arr)
    print(max_number)
    # print(max_number)
    empty_arr = [0] * 100
    print(empty_arr)
    # print(empty_arr)
    for i in range(len(arr)):
        index = arr[i]
        empty_arr[index] += 1
    print(empty_arr)



def fold_array(array, runs):

    while runs != 0:
        length_array = len(array)

        if length_array % 2 == 0:
            
            front_list = array[:len(array)//2]
            back_list = array[len(array)//2:]
            inverted_back_list = back_list[::-1]
            new_list = [x + y for x, y in zip(front_list, inverted_back_list)]

            array = new_list
            runs-=1


            

        if length_array%2  == 1:
            middle = array[len(array) // 2]

            front_list = array[:len(array) // 2]
            back_list = array[len(array) // 2 + 1:]

            inverted_back_list = back_list[::-1]
            new_list = [x + y for x, y in zip(front_list, inverted_back_list)]

            new_list.append(middle)

            array = new_list
            runs-=1

    return array



def fold_array_perfect(array, runs):
    nums = list(array)
    # print(array)
    for _ in range(runs):
        for a in range(len(nums) // 2):
            
            # print("AAAA: ", a)
            # print(nums[a])
            nums[a] += nums.pop()
    return nums

# fold_array_perfect([1,2,3,4,5], 1)
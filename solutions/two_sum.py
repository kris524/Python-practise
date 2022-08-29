def twoNumberSum(array, targetSum):
    # Write your code here.
    solutions = []
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i]+array[j] == targetSum and i!=j:
                solutions.append(array[i])
                solutions.append(array[j])
                break

            
    return solutions[0:2]


# print(twoNumberSum([3,5,-4, 8,11,1,-1,6], 10))


def twoNumberSum2(array, targetSum):
    nums = {}
    for num in array:
        potentialTarget = targetSum - num
        if potentialTarget in nums:
            print(nums)
            return [potentialTarget, num]

        else:
            nums[num] = True
    return []
     
# print(twoNumberSum2([3,5,-4, 8,11,1,-1,6], 10))



def twoNumberSum3(array, targetSum):
    # Write your code here.
    array.sort()
    i = 0
    j = len(array)-1
    while i<j:
        if array[i] + array[j] == targetSum:
            return [array[i], array[j]]
        if array[i] + array[j] > targetSum:
            j-=1
            #move the right boundry
        elif array[i] + array[j] < targetSum:
            i+=1
    return []
        
            #move the left boundry
    
print(twoNumberSum3([3,5,-4, 8,11,1,-1,6], 10))




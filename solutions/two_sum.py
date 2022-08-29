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
    # Write your code here.
    # solution = []
    for i in array:
        j = targetSum - i 
        if j in array and i!=j:
            # solution.append(i)
            # solution.append(j)
            return [i, j]
    return []

            
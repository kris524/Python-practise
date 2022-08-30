def sortedSquaredArray(array):
    # Write your code here.
    # return [
    squared_array = []
    for i in array:
        squared_array.append(i*i)
    return sorted(squared_array)


def sortedSquaredArray2(array):
    # Write your code here.
    # return [
    squared_array = []
    # squared_indx = 0
    for i in range(len(array)):
        #check if the currrent element is smaller than the previous one every run
        print(i)
        # if squared_indx == 0:
        if i == 1:
            squared_indx = 0

        squared_array.append(i*i)

        # if i == squared_indx:
        #     continue
        # print(squared_indx)
        if squared_indx is not None:
            if squared_array[i] < squared_array[squared_indx]:
                #swap them in here
                first_value = squared_array[i]
                second_value = squared_array[squared_indx]
                squared_array[i] = second_value

        
        squared_indx+=1

    return squared_array
            

        #[1,4,9,25,5]

    # return sorted(squared_array)

# print(sortedSquaredArray2([1,2,3,4,5,6,8,9]))

def sortedSquaredArray(array):
    sortedSquare = list(range(len(array)))
    smaller_index = 0
    large_index = len(array) - 1

    for index in reversed(range(len(array))):
        smallerValue = array[smaller_index]
        largetValue = array[large_index]

        if abs(smallerValue) > abs(largetValue):
            sortedSquare[index] = smallerValue*smallerValue
            smaller_index+=1
        else:
            sortedSquare[index] = largetValue*largetValue
            large_index-=1
    return sortedSquare


[-7,-5,-4,3,6,8,9]
[9,16,25,36,49,64,81] 
array =[1, 2, 3, 5, 6, 8, 9]


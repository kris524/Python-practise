

def fold_array(array, runs):

   
    if len(array) % 2 == 0:
        runs = runs - 1
        #TODO
        front_list = array[:len(array)//2]
        back_list = array[len(array)//2:]
        inverted_back_list = back_list[::-1]
        # print(front_list, inverted_back_list)
        new_list = [x + y for x, y in zip(front_list, inverted_back_list)]
        # 
        # print(runs)
        
        if runs == 0:
            # print("HERE")
            # print(new_list)
            return new_list
        else:
            fold_array(new_list, runs)

    else:
        
        middleIndex = (len(array) - 1)/2
        # print(middleIndex)

        front_list = array[0:int(middleIndex)]

        back_list = array[int(middleIndex)+1:]
        inverted_back_list = back_list[::-1]
        print(front_list, back_list[::-1])
        new_list = [x + y for x, y in zip(front_list, inverted_back_list)]

        # print(new_list)
        middle_number = array.pop(int(middleIndex))
        new_list.append(int(middle_number))
        print(new_list)
        # runs = runs - 1
        # fold_array(new_list, runs )



    



    
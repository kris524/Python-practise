# class Solution:
def search(nums, target: int, upper,lower ) -> int:

        if upper>=lower:

            mid = (upper+lower)//2
            print("MID: ", mid)

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return search(nums, target, upper, mid)
            
            elif nums[mid] > target:
                return search(nums, target,mid, lower )
        else:
            return -1


array =[-1,0,3,5,9,12]

print(search(array,9,len(array)-1, 0))

def search2(nums, target: int, upper,lower ) -> int:

        if upper>=lower:

            mid = (upper+lower)//2
            print("MID: ", mid)

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return search(nums, target, upper, mid)
            
            elif nums[mid] > target:
                return search(nums, target,mid, lower )
        else:
            return -1


array =[-1,0,3,5,9,12]

print(search(array,9,len(array)-1, 0))
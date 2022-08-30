# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #[0,0,0,1,1]
        high = n
        low = 1

        while high>=low:
            mid = (high+low)//2
            print(mid)

            if isBadVersion(mid) == False:
                print("LOW", low)
                low = mid+1
                print("NEW LOW", low)

            if isBadVersion(mid) == True:
                high = mid

            if high==low:
                return high
        


            
            
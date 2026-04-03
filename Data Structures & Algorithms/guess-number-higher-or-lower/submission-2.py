# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Binary search over n
        # l is 0 and r is n

        l, r = 0, n
        print(r)

        while l <= r:
            mid = l + (r-l)//2

            

            # Guess is exact pick
            if guess(mid) == 0:
                print("Target achieved: ", guess(mid))
                return mid
            # Guess is greater than pick
            elif guess(mid) == -1:
                print("Go lower: ", guess(mid))
                r = mid - 1
            # Guess is less than pick
            else:
                print("Go higher: ", guess(mid))
                l = mid + 1

    

        
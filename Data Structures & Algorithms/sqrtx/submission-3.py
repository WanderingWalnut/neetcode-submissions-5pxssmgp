class Solution:
    def mySqrt(self, x: int) -> int:
        # Set l and r to 0 and x
        # Calc mid, square the mid
        # If mid == x, return mid
        # Else move l and r based on answer

        # Figure out nearest square i.e 13 -> 9
        def nearest_square(num: int):
            answer = 0
            while (answer+1)**2 <= num:
                answer +=1 

            return answer**2

        x = nearest_square(x)
        l, r = 1, x

        # 0^2 is always 0
        if x == 0:
            return 0

        while l <= r:
            mid = l + (r-l)//2
            print(f"{l} + {r} - {l}//2 = {mid}")

            squared = mid ** 2
            # Squared num is our target
            if squared == x:
                return mid
            # Squared num is too high
            elif squared > x:
                r = mid - 1
                print("Moving R: ", r)
            # Squared num is too low
            else:
                l = mid + 1
                print("Moving L: ", l)
        
        return mid


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterate through both lists
        # Create the sum of nums - 1,2,3 is 321 -> 10x on each additional index
        # Add both nums
        # len of nums becomes our len of linked list
        # i.e Input: l1 = [1,2,3], l2 = [4,5,6] becomes 975
        # Our final list would be size 3
        # Input: l1 = [9], l2 = [9], sum of nums is 18 and list would be size 2
        # Output: [8,1]
        # Turn our sum nums into a str, iterate over each int
        # Rewrite any list or create a new list entirely

        l1Sum = 0
        l2Sum = 0
        sumNums = 0
        res = []

        # Sum from l1
        mul = 1
        while l1 is not None:
            l1Sum += (l1.val * mul)
            mul *= 10
            l1 = l1.next
        print(l1Sum)

        # Sum from l2
        mul = 1
        while l2 is not None:
            l2Sum += (l2.val * mul)
            mul *= 10
            l2 = l2.next
        print(l2Sum)

        sumNums = l1Sum + l2Sum
        print("Sum of Nums: ", sumNums)

        strNums = str(sumNums)
        strNums = strNums[::-1] # Reverse str nums
        print(strNums)

        # Create new list
        for num in strNums:
            node = ListNode(int(num))
            res.append(node)
        
        # Set next ptrs to complete list, do in reverse
        for i in range(len(res)):
            # Point to next node if it exists
            if i < len(res) - 1:
                res[i].next = res[i+1]
            # End of list, point to None
            else:
                res[i].next = None
        
        head = res[0]
        return head
            




        
        
        
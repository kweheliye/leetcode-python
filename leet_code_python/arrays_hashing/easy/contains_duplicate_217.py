class Solution(object):
    def findDuplicate(self, nums):
       hashset = set()

       for num in nums:
           if num in hashset:
               return num

           hashset.add(num)

       return None

hashset = {1, 2, 3}
result = 1  in hashset
print(result)

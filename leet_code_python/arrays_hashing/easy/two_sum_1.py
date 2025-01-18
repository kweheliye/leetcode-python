from collections import defaultdict


def two_sum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i


old = ['a' , 'b' ,'a', 'c', 'b', 'a']

new = list(defaultdict.fromkeys(old).keys())

print(new)
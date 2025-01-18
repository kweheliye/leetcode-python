class Solution:
    def topKFrequent_sorting(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num)

        arr = []

        for num, cnt in count.items():
            arr.append([cnt,num])

        sorted(arr)

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res





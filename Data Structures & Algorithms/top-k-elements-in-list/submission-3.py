class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        l = sorted(d.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(l[i][0])
        return result

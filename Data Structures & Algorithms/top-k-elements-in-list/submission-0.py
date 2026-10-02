class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # for i in range(len(nums)):
        group = []
        c = Counter(nums)
        for i in range(1, k+1):
            res = c.most_common(i)
            char, num = res[i-1]
            group.append(char)
        return group
        
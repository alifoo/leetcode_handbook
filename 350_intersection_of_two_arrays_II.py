class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        c = Counter(nums1)
        intersect = []
        for n in nums2:
            if c[n] > 0:
                intersect.append(n)
                c[n] -= 1
        return intersect

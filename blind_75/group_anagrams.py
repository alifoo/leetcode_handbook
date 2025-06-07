class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        """
        a = 80 -> 0, because 80 - 80
        b = 81 -> 1, 81 - 80
        ord converts a single unicode character into int
        we're working with only english alphabet letters so it's possible
        """
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())

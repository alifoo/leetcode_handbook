class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = []
        for n in heights:
            expected.append(n)

        for i in range(len(expected)):
            swapped = False
            for j in range(len(expected) - i - 1):
                if expected[j] > expected[j + 1]:
                    expected[j], expected[j + 1] = expected[j + 1], expected[j]
                    swapped = True
            if not swapped:
                break
        count = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count += 1
        return count

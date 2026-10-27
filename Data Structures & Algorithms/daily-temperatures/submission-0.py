class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        points_q = []
        max_q = []
        result = [1]*len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while max_q and  max_q[-1] <= temperatures[i]:
                max_q.pop()
                result[i] += points_q.pop()
            if not max_q:
                result[i] = 0

            points_q.append(result[i])
            max_q.append(temperatures[i])
        return result
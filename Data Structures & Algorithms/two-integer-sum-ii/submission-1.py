class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        array_length = len(numbers) 
        for i in range(array_length - 1):
            left = i + 1
            right = array_length - 1
            look_for = target - numbers[i]
            if numbers[right] < look_for:
                continue
            
            while right - left > 1:
                point = (right + left) // 2
                if numbers[point] == look_for :
                    return [i + 1, point + 1]
                elif numbers[point] > look_for:
                    right = point
                else:
                    left = point



            for j in range(i + 1, array_length):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
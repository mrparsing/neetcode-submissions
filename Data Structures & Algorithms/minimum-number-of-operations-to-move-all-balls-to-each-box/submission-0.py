class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        sum_left = [0] * (len(boxes) + 1)
        sum_index_left = [0] * (len(boxes) + 1)

        for i in range(len(boxes)):
            sum_left[i + 1] = sum_left[i] + (boxes[i] == '1')
            sum_index_left[i + 1] = sum_index_left[i] + (i if boxes[i] == '1' else 0)
        
        res = [0] * len(boxes)

        for i in range(len(boxes)):
            left = sum_left[i]
            left_sum = sum_index_left[i]

            right = sum_left[len(boxes)] - sum_left[i+1]
            right_sum = sum_index_left[len(boxes)] - sum_index_left[i+1]

            res[i] = (i * left - left_sum) + (right_sum - i * right)
        return res
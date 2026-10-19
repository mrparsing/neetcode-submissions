class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_index = max(max(seats), max(students)) + 1
        count_seats = [0] * max_index
        count_students = [0] * max_index

        for s in seats:
            count_seats[s] += 1
        for s in students:
            count_students[s] += 1
        
        i = j = res = 0
        remain = len(seats)
        while remain:
            if count_seats[i] == 0:
                i += 1
            if count_students[j] == 0:
                j += 1
            if count_seats[i] and count_students[j]:
                res += abs(i - j)
                count_seats[i] -= 1
                count_students[j] -= 1
                remain -= 1
        return res
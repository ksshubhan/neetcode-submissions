class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0

        intervals.sort()
        
        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            if current_interval[1] <= intervals[i][0]:
                current_interval = intervals[i]
            elif current_interval[0] >= intervals[i][1]:
                current_interval = intervals[i]
            else:
                if current_interval[1] < intervals[i][1]:
                    remove += 1
                else:
                    current_interval = intervals[i]
                    remove += 1 
        
        return remove

                
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if start_j is in start_i and end_i start_i and end_i2 becomes new list
        # how to check if overlapping, sort then compare
        # merge them else keep it
        # [min(start_i, start_j), max(end_i, end_j)]
        
        intervals.sort() # nlogn sort of intervals
        result = [] # final list of merged intervals

        # iterate through intervals
        for i in range(len(intervals)):
            # if result doesnt exist or intervals are not overlapping
            if not result or intervals[i][0] > result[-1][1]:
                result.append( [intervals[i][0], intervals[i][1]] )
            # compare previously added list to current iteration
            else:
                result[-1][1] = max(result[-1][1],intervals[i][1])
        
        return result
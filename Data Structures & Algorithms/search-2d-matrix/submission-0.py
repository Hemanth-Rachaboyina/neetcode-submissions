class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        final = []

        for i in matrix :
            for j in i:
                final.append(j)
        
        l = 0
        r = len(final)-1

        while l<=r:
            m = (l+r)//2
            if final[m] > target:
                r = m-1
            if final[m]<target:
                l = m+1
            if final[m]==target:
                return True
        return False
        
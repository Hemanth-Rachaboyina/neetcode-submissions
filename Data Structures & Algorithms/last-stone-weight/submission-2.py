class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            num1 = max(stones)
            stones.remove(num1)
            num2 = max(stones)
            stones.remove(num2)

            if num1 == num2:
                pass
            if num1 != num2 : 
                stones.append(abs(num1-num2))
            # else:
            #     stones.append(num2-num1)
            
        
        if len(stones) == 1:
            return max(stones)
        else:
            return 0
        

        
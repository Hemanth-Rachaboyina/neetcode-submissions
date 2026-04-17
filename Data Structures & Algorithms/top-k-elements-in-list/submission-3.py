class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = {}
        # final = []
        for i in nums :
                if i in hm :
                        hm[i] = hm[i]+1
                else:
                        hm[i] = 1

        print(hm)

        vls = list(hm.values())
        vls.sort(reverse = True)
        vls = vls[:k]

        print("vls",vls)
        keys = [k for k, v in hm.items() if v in vls]

        # for i in vls:
        #         for key,value in hm.items():
        #                 if value == i:
        #                         final.append(key)
                
        return keys

        
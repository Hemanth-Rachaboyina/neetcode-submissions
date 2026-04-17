class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}
        final=[]

        for s in strs:
            anagram = "".join(sorted(s))
            if anagram in hm:
                hm[anagram].append(s)
            else:
                hm[anagram] = [s]
                

        print(hm)

        for key, values in hm.items():
            final.append(values)


        return final
            

        
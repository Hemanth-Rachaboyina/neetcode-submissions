class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for i in strs :
            final_str = final_str + chr(257) +  i 
        
        return final_str


    def decode(self, s: str) -> List[str]:
        return s.split(chr(257))[1:]

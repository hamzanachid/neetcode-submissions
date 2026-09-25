class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs== [""]:
            return "void"
        if( strs==[]):
            return "empty"
        s='~'.join(strs)
        return s

    def decode(self, s: str) -> List[str]:
        if s== "void":
            return [""]
        if(s=="empty"):
            return []
        return s.split('~')
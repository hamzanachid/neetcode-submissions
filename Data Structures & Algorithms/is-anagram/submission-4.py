class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       chars="azertyuiopmlkjhgfdsqwxcvbn"
       same=True
       for i in chars:
        if not(s.count(i)==t.count(i)):
            same=False
            break
       return same     
        
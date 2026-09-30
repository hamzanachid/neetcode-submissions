class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s:
            if i in "azertyuiopmlkjhgfdsqwxcvbn1234567890AZERTYUIOPMLKJHGFDSQWXCVBN":
             t+=i
        print(t)
        print(t[::-1])     
        return t[::-1].lower()==t.lower()

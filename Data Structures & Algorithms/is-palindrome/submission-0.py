class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_c = ''
        for i in s:
            if i.isalnum():
                new_c += i.lower()
        return new_c == new_c[::-1]

             

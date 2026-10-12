class Solution:
    def isPalindrome(self, s: str) -> bool:
        listt = []
        second = []

        for i in s:

            if i.isalnum():
                listt.append(i.lower())
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                second.append(s[i].lower())
        return second == listt

        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""

        for c in s.lower():
            if c.isalnum():
                palin += c

        if palin == "":
            return True

        lis_palin = list(palin)
        rev_palin = lis_palin.copy()
        rev_palin.reverse()
        return lis_palin == rev_palin


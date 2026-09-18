class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(filter(str.isalnum, s)).lower()
        str_lenght = len(clean_str)
        for i in  range(str_lenght // 2):
            if clean_str[i] != clean_str[str_lenght - i - 1]:
                return False
        return True
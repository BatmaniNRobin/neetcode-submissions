class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create new string and iterate through old
        # and if isalnum then add to new str and make .lower
        # then use two pointers to check if is palindrome
        new_str = ''

        for char in s:
            if char.isalnum():
                new_str += char.lower()
        
        return new_str == new_str[::-1]
class Solution:
    def isValid(self, s: str) -> bool:
        args = deque()
        openings = { # dict for O(1) lookup
            ']': '[',
            '}': '{',
            ')': '('
        }

        for char in s:
            if char in openings:
                if args and args[-1] == openings[char]:
                    args.pop()
                else:
                    return False
            else:
                args.append(char)
        return True if not args else False        
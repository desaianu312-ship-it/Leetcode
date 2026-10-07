from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = {s}

        while queue:
            valid = []

            for string in queue:
                if is_valid(string):
                    valid.append(string)

            if valid:
                return list(set(valid))

            next_level = set()

            for string in queue:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i + 1:])

            queue = next_level

        return [""]
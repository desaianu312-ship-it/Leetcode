class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            res = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    part, i = parse(i + 1)
                else:
                    part = {expression[i]}
                    i += 1

                # Concatenation
                res = {
                    a + b
                    for a in res
                    for b in part
                }

                if i < len(expression) and expression[i] == ',':
                    break

            if i < len(expression) and expression[i] == '}':
                i += 1

            # Handle union inside braces
            return res, i

        def expand(s):
            # Recursive descent with:
            # union = '+'
            # concatenation = '*'

            pos = 0

            def expression():
                nonlocal pos

                result = term()

                while pos < len(s) and s[pos] == ',':
                    pos += 1
                    result |= term()

                return result

            def term():
                nonlocal pos

                result = {""}

                while pos < len(s) and s[pos] not in "},":
                    if s[pos] == '{':
                        pos += 1
                        part = expression()
                        pos += 1          # skip '}'
                    else:
                        part = {s[pos]}
                        pos += 1

                    result = {
                        a + b
                        for a in result
                        for b in part
                    }

                return result

            return expression()

        return sorted(expand(expression))
        
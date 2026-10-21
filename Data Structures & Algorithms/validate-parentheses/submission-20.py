class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {")":"(", "]":"[", "}":"{"}

        for c in s:
            print(f"0Char is {c}")
            if len(stack) < 1:
                print(f"Adding {c} to the stack")
                stack.append(c)
                continue

            if c in chars.keys():
                print(f"will we pop {stack[-1]} because c is {c}")

                if stack[-1] == chars[c]:
                    print(f"Popping {chars[c]} because c is {c}")
                    stack.pop()
                else:
                    print(f"1Adding {c} to the stack")
                    stack.append(c)

            else:
                print(f"2Adding {c} to the stack")
                stack.append(c)

        return len(stack) == 0

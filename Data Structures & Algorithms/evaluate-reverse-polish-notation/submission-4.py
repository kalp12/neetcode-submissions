class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == "+":
                a = int(s.pop())
                b = int(s.pop())
                s.append(a + b)
            elif t == "*":
                a = int(s.pop())
                b = int(s.pop())
                s.append(a * b)
            elif t == "-":
                a = int(s.pop())
                b = int(s.pop())
                s.append(b - a)
            elif t == "/":
                a = int(s.pop())
                b = int(s.pop())
                s.append(int(b / a))
            else:
                s.append(int(t))
        return s[0]
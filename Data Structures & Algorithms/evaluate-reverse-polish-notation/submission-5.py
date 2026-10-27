class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        first_op = second_op = 0
        q = list()

        for c in tokens:
            if c == "+":
                second_op = q.pop(-1)
                first_op = q.pop(-1)
                res = first_op + second_op
            elif c == "-":
                second_op = q.pop(-1)
                first_op = q.pop(-1)
                res = first_op - second_op
            elif c == "*":
                second_op = q.pop(-1)
                first_op = q.pop(-1)
                res = first_op * second_op
            elif c == "/":
                second_op = q.pop(-1)
                first_op = q.pop(-1)
                res = int(first_op / second_op)
            else:
                res = int(c)
            q.append(res)
        return res


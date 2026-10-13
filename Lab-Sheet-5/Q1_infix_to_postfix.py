def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    output, stack = [], []
    for token in expression.replace(" ", ""):
        if token.isalnum(): output.append(token)
        elif token == "(": stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(": output.append(stack.pop())
            if not stack: raise ValueError("Mismatched parentheses")
            stack.pop()
        elif token in precedence:
            while stack and stack[-1] != "(" and (precedence[stack[-1]] > precedence[token] or (precedence[stack[-1]] == precedence[token] and token != "^")):
                output.append(stack.pop())
            stack.append(token)
        else: raise ValueError("Unsupported character: " + token)
    while stack:
        if stack[-1] == "(": raise ValueError("Mismatched parentheses")
        output.append(stack.pop())
    return "".join(output)

if __name__ == "__main__":
    expr = input("Enter infix expression [A+(B*C)]: ").strip() or "A+(B*C)"
    print("Postfix expression:", infix_to_postfix(expr))

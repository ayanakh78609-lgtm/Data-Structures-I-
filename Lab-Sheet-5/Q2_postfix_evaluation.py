def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.lstrip("-").isdigit(): stack.append(int(token)); continue
        if token not in {"+", "-", "*", "/", "^"}: raise ValueError("Use space-separated integers and operators")
        if len(stack) < 2: raise ValueError("Invalid postfix expression")
        b, a = stack.pop(), stack.pop()
        if token == "+": stack.append(a + b)
        elif token == "-": stack.append(a - b)
        elif token == "*": stack.append(a * b)
        elif token == "/":
            if b == 0: raise ZeroDivisionError("Division by zero")
            stack.append(int(a / b))
        elif token == "^": stack.append(a ** b)
    if len(stack) != 1: raise ValueError("Invalid postfix expression")
    return stack[0]

if __name__ == "__main__":
    expr = input("Enter space-separated postfix expression [2 3 * 5 4 * + 9 -]: ").strip() or "2 3 * 5 4 * + 9 -"
    print("Result:", evaluate_postfix(expr))

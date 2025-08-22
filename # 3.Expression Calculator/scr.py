def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expression):
    stack = []
    output = []
    for token in expression:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
    return stack[0]

def main():
    expr = input("Enter expression (e.g. 3+5*(2-1)): ")
    tokens = []
    number = ""
    for ch in expr:
        if ch.isdigit():
            number += ch
        else:
            if number:
                tokens.append(number)
                number = ""
            if ch.strip():
                tokens.append(ch)
    if number:
        tokens.append(number)
    postfix = infix_to_postfix(tokens)
    print("Postfix:", " ".join(postfix))
    result = evaluate_postfix(postfix)
    print("Result:", result)

if __name__ == "__main__":
    main()


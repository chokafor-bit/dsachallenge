def balance_bracket(text):
    # pass 
    stack = []
    for char in text:
        if char in "([{":
            stack.append(char)

        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
        
            stack.pop()
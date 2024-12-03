#Python code
def isValidParenthesis(s: str) -> bool:
    x=['{','(','[']
    stack=[]
    for i  in s:
        if i in x:
            stack.append(i)
        elif stack and i=='}' and stack[-1]=='{':
            stack.pop()
        elif stack and i==']' and stack[-1]=='[':
            stack.pop()
        elif stack and i==')' and stack[-1]=='(':
            stack.pop()        
        else:
            stack.append(i)
    return len(stack)==0      



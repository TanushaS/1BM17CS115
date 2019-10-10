def is_valid(str):
    stack,pchar=[],{"(":")","{":"}","[":"]"}
    for p in str:
        if p in pchar:
            stack.append(p)
        elif len(stack)==0 or pchar[stack.pop()]!=p:
            return False
    return len(stack)==0
    
exp=input("Enter the expression:")
if is_valid(exp):
    print("The expression is valid")
else:
    print("The expression is not valid")    
           

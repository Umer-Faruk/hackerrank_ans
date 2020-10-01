def isBalanced(s):
    l = []
    op = ['[', '(', '{']
    cp = [']', ')', '}']
    ecb = 0
    for i in s:
        if i in op:
            l.append(i)
        elif i in cp:
            try:
                if i == ')' and l[-1] == '(':
                    print("()pair")
                    l.pop()
                elif i == '}' and l[-1] == '{':
                    print("{}pairs")
                    l.pop()
                elif i == ']' and l[-1] == '[':
                    print("[]pairs")
                    l.pop()
                else:
                    ecb += 1
            except:
                return "NO"

    print(l)
    if len(l) == 0 and ecb == 0:
        return "YES"
    else:
        return "NO"

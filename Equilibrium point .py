def solve(l):
    if len(l)==1:
            return 1
            # print(l[0])
    elif len(l)<=2:
            return -1
            # print(-1)
    else:
            for i in range(1,len(l)):
                # print(l[:i],l[i+1:])
                if sum(l[:i])==sum(l[i+1:]):
                    return (i+1)
                    
                else:
                    continue
    
    return -1

def sol2(l):
    d={}

    if len(l)==1:
        return 1
    elif len(l)<=2:
        return -1
    else:
         


              
    

    
for t in range(int(input())):
#     n = input()
#     l=list(map(int,input().split()))
    # print(solve(l))

    l=[1,3,5,2,2]
    r =sol2(l)
    


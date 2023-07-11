inp=int(input())
temp=0
print(inp,end=" ")
while(inp>1):
    if inp%2==0:
        inp=inp//2
        print(inp,end=" ")
    elif(inp%2)!=0:
        inp=(3*inp)+1
        print(inp,end=" ")

for t in range (int(input())):
    n,b=map(int,input().split())
    arr=list(map(int,input().split()[:n]))
    c=0;
    arr.sort()
    for i in arr:
        if i<=b:
            b=b-i
            c+=1
        else:
            break
    print("Case #"+str(t+1)+": "+str(c))
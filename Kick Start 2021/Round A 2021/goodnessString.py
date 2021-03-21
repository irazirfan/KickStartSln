t =int(input())
o=[]
for i in range(0,t):
    ss = list(map(int, input().rstrip().split()))
    n = ss[0]
    k = ss[1]
    s = str(input())
    c=0
    
    s1=s[0:len(s)//2]
    s2=s[len(s)//2 if len(s)%2 == 0 else ((len(s)//2)+1):]
    s3=list(s2)
    s3.reverse()
    s2=''.join(s3)
    for i in range(0, len(s1)):
        if(s1[i]!=s2[i]):
            c+=1
    o.append(abs(k-c))
    
for p in range(0, t):
    print("Case #"+str(p+1)+": "+str(o[p]))
n= int(input())
x=list(map(int, input().split()))
s,c=0,0
nsd,psd=0,0
maxim,maxpos=0,0
for i in range(n):
    if x[i]==1:
        s+=1
        c+=1
        if s>nsd:
            nsd=s
            psd=i+1
    else:
        c+=1
        s-=1
        if s==0:
            if c>maxim:
                maxim=c
                maxpos=i-c+2
            c=0
print(nsd,psd,maxim,maxpos)

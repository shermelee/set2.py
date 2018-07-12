N=int(input())
K=int(input())
l=[]
sum=0
for i in range(N):
    x=int(input())
    l.append(x)
for i in range(K):
    sum=sum+l[i]
print(sum)

n = int(input())
f=[]
c=0
for i in range (n):
   dist = list(map(int, input().split()))
   f.append(dist)
for i in range(n) :
    t=f[i][0]
    for x in f[i]:
       if x > t:
          c +=1
    print(c)
    c=0

    
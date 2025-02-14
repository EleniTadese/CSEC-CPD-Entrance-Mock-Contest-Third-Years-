n = int(input())

my_list = []

for i in range (n):
    a = list(map(int,input().split()))
    my_list.append(a)
for i in range(n):
    k=my_list[i]
    for j in k:
        if j != max(k) and j != min(k):
            print(j)
            continue



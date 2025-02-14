
n, m = map(int, input().split())  
grid = [input().strip() for _ in range(n)] 

top = n
bottom = -1
left = m
right = -1

for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)

for i in range(top, bottom + 1):
    print(grid[i][left:right + 1])

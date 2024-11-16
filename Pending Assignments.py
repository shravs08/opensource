X, Y, Z = map(int, input().split())
t = X * Y
ta = Z * 1440
if t <= ta:
    print("YES")
else:
    print("NO")

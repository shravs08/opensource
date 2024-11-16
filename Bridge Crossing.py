X, Y, Z = map(int, input().split())
if Z > Y:
    m = (Z - Y) // X
    print(m)
else:
    print(0)

n = 6
#k = 0
left = n/2
right = n*3 - n/2
for i in range(0, n*2):
    k = 0
    for j in range(0, i):
        k += 1
        if k > left:
            print(".", end="")
    for j in range(0, n):
        k += 1
        if k > left and k < right:
            print("*", end="")
    for j in range(k+1, n*3):
        k += 1
        if k < right:
            print(".", end="")
    print("\n")
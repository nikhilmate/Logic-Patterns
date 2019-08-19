def findMax(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max

def compute(n, k):
    arr = []
    result = 0
    el = ['a', 'b', 'c']
    for m in el:
        tempCompute = []
        finalResult = 0
        for i in range(0, len(n)):
#             print("i",i)
            changeCount = 0
            length = 0
            for j in range(i, len(n)):
#                 print("j",j)
                if n[j] == m:
                    length += 1
                else:
                    if changeCount + 1 > k:
                        break
                    else:
                        length += 1
                        changeCount += 1
#                 print("j length", length, changeCount)
#             print("i length", length)
            tempCompute.append(length)
        finalResult = findMax(tempCompute)
        arr.append(finalResult)
#         print(finalResult)
        
    result = findMax(arr)
    return result

n = 'aabaacaaccacccc'
n = [x for x in n]
print(n)
k = 2
print(compute(n, k))

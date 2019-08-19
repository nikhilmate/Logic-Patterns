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
        for i in range(0, len(n) - 1):
            changeCount = 0
            length = 0
            for j in range(i+1, len(n)):
                if changeCount <= k:
                    if n[j] == m:
                        length += 1
                    else:
                        length += 1
                        changeCount += 1
                else:
                    changeCount = 0
                    break
            tempCompute.append(length)
        finalResult = findMax(tempCompute)
        arr.append(finalResult)
        
    result = findMax(arr)
    return result

n = 'aabaacaaaabbbbabbb'
n = [x for x in n]
print(n)
k = 1
print(compute(n, k))
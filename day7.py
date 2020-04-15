def countElements(sarr):
    hashTable = {}
    counter = 0
    for i in arr:
        if i not in hashTable:
            hashTable[i] = 1
        else:
            hashTable[i] += 1
            
    seen = []
    for i in range(len(arr)):
        if arr[i]+1 in hashTable and arr[i] not in seen:
            counter += hashTable[arr[i]]
            seen.append(arr[i])
    return counter
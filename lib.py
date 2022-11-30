def findRepeats(array):
    result = set()
    for i in array:
        for j in array:
            if i is not j:
                result |= set(i) & set(j)
    return result
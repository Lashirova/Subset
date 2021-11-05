def arrayAddition(arr, s):
    sets = [[]]
    for num in arr:
        nextPart = []
        for n in sets:
            nextNum = n + [num]
            nextPart.append(nextNum)
            # print('nextNum: {}'.format(nextNum))
            if sum(nextNum) == s:
                return nextNum
        sets += nextPart
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20]
    s = 23
    sets = arrayAddition(arr, s)
    print(sets)
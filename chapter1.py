
# Is Unique
def isUnique(s):
    letters = set()
    for char in s:
        if (char in letters):
            print(False)
            return False
        else:
            letters.add(char)
    print(True)
    return True

# Check Permutation
def checkPermutation(s1, s2):
    letters = {}

    if (len(s1) != len(s2)):
        return False
    
    for char in s1:
        if (char in letters):
            count = letters.get(char)
            letters[char] = count + 1
        else:
            letters[char] = 1
    for char in s2:
        if (char in letters):
            count = letters.get(char)
            count = count - 1
            if (count == 0):
                del letters[char]
        else:
            print(False)
            return False
    print(True)
    return True

# Palindrome Permutation
def palindromePermutation(s):
    letters = set()
    s = s.lower()
    for i in range(len(s)):
        if (s[i] in letters):
            letters.remove(s[i])
        elif (s[i] == " "):
            continue
        else:
            letters.add(s[i])
    if (len(letters) == 0 or len(letters) == 1):
        return True
    return False

# One Away
def oneAway(s1, s2):
    word = {}
    for char in s1:
        if char in word:
            count = word[char]
            word[char] = count + 1
        else:
            word[char] = 1

    for char in s2:
        if char in word:
            if (word[char] == 1):
                del word[char]
            else:
                count = word[char]
                word[char] = count - 1
        else:
            word[char] = 1
    total = 0
    for value in word.values():
        total = total + value

    if total > 1:
        return False

    return True

# String Compression
def stringCompress(s):
    result = s[0]
    oldChar = s[0]
    count = 0
    for char in s:
        if (char == oldChar):
            count = count + 1
        else:
            result = result + str(count) + char
            count = 1
        oldChar = char
    return result + str(count)

# URLify
def URLify(s):
    s = s.replace(" ", "%20")
    return s

# RotateMatrix
def rotateMatrix(arr):
    # Transpose
    for i in range(0, len(arr)):
        for j in range(i, len(arr[0])):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    # Reverse Each Row
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0]) // 2):
            arr[i][j], arr[i][len(arr[0]) - j  - 1] = arr[i][len(arr[0]) - j  - 1], arr[i][j]

    return arr


# Zero Matrix
def zeroMatrix(arr):
    rows = set()
    cols = set()
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if arr[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if (i in rows or j in cols):
                arr[i][j] = 0
    return arr

# String Rotation
def stringRotation(a, b):
    aa = a + a
    return len(a) == len(b) and b in aa







    






    


def main():




    '''
    a = "waterbottle"
    b = "erbottlewat"
    print(stringRotation(a, b))
 


    arr = [[0, 0, 3], [4, 5, 6], [7, 8, 9]]
    print(zeroMatrix(arr))
 
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotateMatrix(arr))

    a = "Mr John Smith"
    print(URLify(a))

    a = "abcdefg"
    b = "abcdefga"
    isUnique(a)
    isUnique(b)

    a = "racecar"
    b = "accarer"
    c = "ecarf"
    checkPermutation(a, b)
    checkPermutation(a, c)

    a = "Tact Coa"

    print(palindromePermutation(a))

    s1 = "pale"
    s2 = "bale"
    print(oneAway(s1, s2))

    s = "aaaaabzcdcc"
    print(stringCompress(s))
    '''



main()
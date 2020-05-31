
def binarySearch(data, value):
    value = int (value)
    start = 0
    end = len(data) - 1

    while (start <= end):
        mid = int((start + end) / 2)
        if (data[mid] == value):
            print("Found Value: ", value)
            return data[mid]
        elif (data[mid] < value):
            start = mid + 1
        else:
            end = mid - 1
    
    print("Value is not in Data")


def main():
    binarySearch([1, 3, 5, 7, 9], 1)
    binarySearch([1, 3, 5, 7, 9], 5)
    binarySearch([1, 3, 5, 7, 9], 9)
    print()
    binarySearch([1, 3, 5, 7, 9, 11], 1)
    binarySearch([1, 3, 5, 7, 9, 11], 5)
    binarySearch([1, 3, 5, 7, 9, 11], 9)
    binarySearch([1, 3, 5, 7, 9, 11], 11)
    print()
    binarySearch([1, 3, 5, 7, 9, 11], 2)
    binarySearch([1, 3, 5, 7, 9, 11], 4)
    binarySearch([1, 3, 5, 7, 9, 11], 6)
    binarySearch([1, 3, 5, 7, 9, 11], 8)
    binarySearch([1, 3, 5, 7, 9, 11], 10)

main()



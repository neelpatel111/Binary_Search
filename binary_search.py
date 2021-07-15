A = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
n = int(input("Search element you want to find it "))

def BinarySearch(A, n):
    low = 0
    mid = 0
    high = len(A) - 1


    while low <= high:

        mid = (high + low)//2

        if A[mid] < n:

            low = mid + 1

        elif A[mid] > n:

            high = mid - 1

        else:
            return mid

    return -1



result = BinarySearch(A, n)

if result != -1:
    print("Element is present at index ", result)

else:
    print("Element not present in list")












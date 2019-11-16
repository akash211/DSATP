def isArrayInSortedOrder(A):
    #Base Case
    if len(A) == 1:
        return True
    return (A[0] <= A[1] and isArrayInSortedOrder(A[1:]))


A = list(map(int, input("Enter the list or Array: \n").split()))
print(isArrayInSortedOrder(A)  )
  
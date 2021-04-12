def insertion_sort(A):
    i=j=0
    size = len(A)
    while i < size:
        for j in range(0, i+1):
            if A[j] > A[i]:
                temp = A[j]
                A[j] = A[i]
                A[i] = temp
        i = i+1
    print(A)
    
A = [11, 9, 29, 7, 2, 15, 28]
insertion_sort(A)

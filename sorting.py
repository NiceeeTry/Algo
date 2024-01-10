def insertionSort(a):
    for i in range(1,len(a)):
        j = i
        x = a[i]
        while j>0 and a[j-1]>x:
            a[j] = a[j-1]
            j-=1
        a[j] = x
        print(a)


a = [1,7,4,2,0,8,32,60]
# insertionSort(a)
# print(a)

def insertionSortB(a):
    for i in range(1,len(a)):
        j = i
        while j>0 and a[j]<a[j-1]:
            a[j-1],a[j] = a[j], a[j-1]
            j-=1

# insertionSortB(a)
# print(a)


def MergeSort(arr):
    if len(arr)>1:
        m = len(arr)//2
        l = arr[:m]
        r = arr[m:]

        MergeSort(l)
        MergeSort(r)

        i = j = k = 0 

        while i<len(l) and j < len(r):
            if l[i]<=r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1

        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k] = r[j]
            k+=1
            j+=1

# MergeSort(a)
# print(a)

def QuickSort(a):
    less = []
    equal = []
    greater = []
    if len(a)>1:

        pivot = a[0]
        for v in a:
            if v < pivot:
                less.append(v)
            elif v == pivot:
                equal.append(v)
            else:
                greater.append(v)

        return QuickSort(less)+equal+QuickSort(greater) 
    else:
        return a

# print(a)
# b = QuickSort(a)
# print(b)


def BubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
# print(a)
# BubbleSort(a)
# print(a)

# print(a)
# BubbleSort_test(a)
# print(a)
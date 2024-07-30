
def max_heapify(A, k):
    l = left(k)
    r = right(k) 
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)
def left(k):
    return 2 * k + 1
def right(i): 
    return 2 * i + 2 
def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A, k)
A = [3, 9, 2, 1, 4, 5]
build_max_heap(A)
print(A)


def insert_min_heap(heap, value):
    heap.append(value)
    index = len(heap) - 1
    while index > 0 and heap[(index - 1) // 2] > heap[index]:
        heap[index], heap[(index - 1) //
                          2] = heap[(index - 1) // 2], heap[index]
        index = (index - 1) // 2


heap = []
values = [10, 7, 11, 5, 4, 13]
for value in values:
    insert_min_heap(heap, value)
    print(f"Inserted {value} into the min-heap: {heap}")
import heapq
# QUESTION 1
def find_kth_smallest_heap(arr, k):
    # Initialize an empty max heap
    heap = []
    for num in arr:
        # Negate the number to simulate a max heap
        heapq.heappush(heap, -num)
        if len(heap) > k:
            # If heap size exceeds k, remove the largest element
            heapq.heappop(heap)
            # The K'th smallest element is at the top of the heap
    return -heap[0]

arr = [7, 2, 5, 3, 4, 8]
k = 3
# Output the 3rd smallest element
print(find_kth_smallest_heap(arr, k))


# QUESTION 2
def sortNearlySortedArray(A, size, k):
	for i in range(1, size):
        # Key element to be inserted
		key = A[i]
		j = i - 1
		while j >= max(0, i - k) and A[j] > key:
            # Move elements greater than key to one position ahead
			A[j + 1] = A[j]
			j -= 1
            # Place key at the correct position
		A[j + 1] = key

	for i in range(size):
        # Print sorted array
		print(A[i], end=' ')

	print()

A = [2, 6, 3, 12, 56, 8]
size = 6
k = 3
# Sort and print the nearly sorted array
sortNearlySortedArray(A, size, k)


# Question 3
def pr_N_mostFrequentNumber(arr, N, K):
    mp = {}
    for i in range(N):
        if arr[i] in mp:
             # Count frequency of each element
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    a = [0] * (len(mp))
    j = 0
    for i in mp:
         # Create list of [element, frequency]
        a[j] = [i, mp[i]]
        j += 1
        # Sort by element values in descending order
    a = sorted(a, key=lambda x: x[0], reverse=True)
    # Sort by frequency in descending order
    a = sorted(a, key=lambda x: x[1], reverse=True)

    print(K, "numbers with most occurrences are:")
    for i in range(K):
         # Print the top K frequent elements
        print(a[i][0], end=" ")

if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    N = 8
    K = 2
    # Output the top 2 most frequent elements
    pr_N_mostFrequentNumber(arr, N, K)




# QUESTION 4
def MaxHeapify(arr, i, N):
	l = 2 * i + 1
	r = 2 * i + 2
	largest = i
	if l < N and arr[l] > arr[i]:
		largest = l
	if r < N and arr[r] > arr[largest]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]  # Swap and heapify
		MaxHeapify(arr, largest, N)

def convertMaxHeap(arr, N):
	for i in range(int((N - 2) / 2), -1, -1):
		MaxHeapify(arr, i, N)  # Build max heap from the bottom up

def printArray(arr, size):
	for i in range(size):
		print(arr[i], end=" ")
	print()

if __name__ == '__main__':
	arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
	N = len(arr)
	print("Min Heap array : ")
	printArray(arr, N)
	convertMaxHeap(arr, N)  # Convert min heap to max heap
	print("Max Heap array : ")
	printArray(arr, N)  # Print the converted max heap

# QUESTION 5
import sys
class MinHeap:
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    def parent(self, pos): 
        return pos//2
  
    def leftChild(self, pos): 
        return 2 * pos 
  
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    def isLeaf(self, pos): 
        return pos*2 > self.size 
  
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    def minHeapify(self, pos): 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
        current = self.size 
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    def minHeap(self): 
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    def remove(self): 
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 

if __name__ == "__main__": 
    print('The minHeap is ') 
    minHeap = MinHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.minHeap() 
    minHeap.Print() 
    print("The Min val is " + str(minHeap.remove()))  # Output the minimum value from the heap


# QUESTION 1
import heapq

def find_kth_smallest_heap(arr, k):
    # Initialize an empty max heap
    heap = []
    for num in arr:
        # Negate the number to simulate a max heap
        heapq.heappush(heap, -num)
        # If the heap size exceeds K, pop the largest element
        if len(heap) > k:
            heapq.heappop(heap)
    # The K'th smallest element is at the top of the heap
    # We negate it again to get the actual value
    return -heap[0]

# Example usage
arr = [7, 2, 5, 3, 4, 8]
k = 3
print(find_kth_smallest_heap(arr, k))


# QUESTION 2
# import heapq
def sortNearlySortedArray(A, size, k):
	for i in range(1, size):
		key = A[i]
		j = i - 1
		while j >= max(0, i - k) and A[j] > key:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key

	for i in range(size):
		print(A[i], end=' ')

	print()


A = [2, 6, 3, 12, 56, 8]
size = 6
k = 3
sortNearlySortedArray(A, size, k)


# QUESTION3
def pr_N_mostFrequentNumber(arr, N, K):

    mp = {}
    for i in range(N):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    a = [0] * (len(mp))
    j = 0
    for i in mp:
        a[j] = [i, mp[i]]
        j += 1
    a = sorted(a, key=lambda x: x[0],
               reverse=True)
    a = sorted(a, key=lambda x: x[1],
               reverse=True)

    print(K, "numbers with most occurrences are:")
    for i in range(K):
        print(a[i][0], end=" ")


if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    N = 8
    K = 2

    pr_N_mostFrequentNumber(arr, N, K)


# A Python3 program to convert min Heap
# to max Heap

# to heapify a subtree with root
# at given index

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
		arr[i], arr[largest] = arr[largest], arr[i]
		MaxHeapify(arr, largest, N)

# This function basically builds max heap


def convertMaxHeap(arr, N):

	# Start from bottommost and rightmost
	# internal node and heapify all
	# internal nodes in bottom up way
	for i in range(int((N - 2) / 2), -1, -1):
		MaxHeapify(arr, i, N)

# A utility function to print a
# given array of given size


def printArray(arr, size):
	for i in range(size):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':

	# array representing Min Heap
	arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
	N = len(arr)

	print("Min Heap array : ")
	printArray(arr, N)

	# Function call
	convertMaxHeap(arr, N)

	print("Max Heap array : ")
	printArray(arr, N)

# This code is contributed by PranchalK
# Python3 implementation of Min Heap 
  

# QUESTION 5
import sys 

class MinHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        return pos*2 > self.size 
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 
  
# Driver Code 
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
    print("The Min val is " + str(minHeap.remove())) 
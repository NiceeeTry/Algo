class Heap():
    def __init__(self):
        self.a = []

    def get_min(self):
        return self.a[0]
    
    def insert(self, num):
        self.a.append(num)
        # sift up
        i = len(self.a) - 1
        while i > 0 and self.a[i] < self.a[(i-1)//2]:
            self.a[i], self.a[(i-1)//2] = self.a[(i-1)//2], self.a[i]
            i = (i - 1) // 2

    def remove_min(self):
        self.a[0] = self.a[-1]
        self.a.pop()  
        n = len(self.a)
        # sift down
        i = 0
        while 2 * i + 1 < n:
            j = 2 * i + 1
            if 2 * i + 2 < n and self.a[2*i+2] < self.a[2*i+1]:
                j = 2 * i+2
            if self.a[i] <= self.a[j]:
                break
            else:
                self.a[i], self.a[j] = self.a[j], self.a[i]
                i = j

def heap_sort(arr):
    h = Heap()
    for v in arr:
        h.insert(v)
    a = []
    for _ in range(len(h.a)):
        a.append(h.get_min())
        h.remove_min()
    return a



arr = [43,11,3,12,4,7,33]
print(arr)
print(heap_sort(arr)) 


# h = Heap()

# h.insert(4)
# h.insert(5)
# h.insert(8)

# h.insert(11)
# h.insert(15)

# h.insert(28)
# h.insert(9)

# h.insert(13)
# h.insert(10)
# h.insert(42)
# h.insert(6)
# h.insert(7)

# print(h.a)
class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.ls = [None]*k
        self.len,self.cur,self.st,self.end = k,0,0,0
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        else: self.cur += 1
        self.ls[self.end] = value
        self.end = self.end + 1 if self.end < self.len-1 else 0
        return True
        
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        else: self.cur -= 1
        self.st = self.st + 1 if self.st < self.len-1 else 0
        return True
        
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.ls[self.st] if not self.isEmpty() else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): return -1
        return self.ls[self.end-1] if self.end != 0 else self.ls[self.len-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if self.cur == 0 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return True if self.cur == self.len else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

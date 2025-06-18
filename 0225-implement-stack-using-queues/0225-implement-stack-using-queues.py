from queue import Queue
class MyStack:

    def __init__(self):
        self.queue = Queue()  # put() | get() | qsize()
        self.queue2 = Queue()
        self.top_val = None
    def push(self, x: int) -> None:
        self.queue.put(x)
        self.top_val = x
    def pop(self) -> int:
        output_v = self.top_val

        
        while self.queue.qsize() > 1:
                val = self.queue.get()
                self.queue2.put(val)
                self.top_val = val
        self.queue.get()
        self.queue, self.queue2 = self.queue2, self.queue
        return output_v

    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        return self.queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
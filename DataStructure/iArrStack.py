class Stack:
    def __init__(self,arr=[]):
        if not isinstance(arr,list) :
           raise ValueError("Initial input must be an array, or no input.")
        self.stk = arr
        self.size=len(arr)
    def __str__(self) -> str:
        string = ""
        for i in range(0, self.size):
            string += str(self.stk[i]) + " "
        return string
    def push(self,num):
        self.stk.append(num)
        self.size+=1
    def pop(self):
        if(not self.empty()):
            a=self.stk.pop()
            self.size-=1
            return a
        else: 
            return None
    def top(self):
        if(not self.empty()): return self.stk[self.size-1]
        else: return None
    def empty(self):
        return True if self.size==0 else False
    def clear(self):
        self.stk.clear()
        self.size=0
            

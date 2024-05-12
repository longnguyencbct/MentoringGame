from DataStructure.iSLL import SLL
class SLLStack:
    def __init__(self,arr=[]):
        if not isinstance(arr,list) :
           raise ValueError("Initial input must be an array, or no input.")
        self.stk = SLL(arr)
    def __str__(self) -> str:
        string="SLLStack(["
        curr=self.stk.head
        while(curr!=None):
            string+=str(curr.data)+", "
            curr=curr.next
        if(self.stk.size!=0):
            string=string[:-2]
        string+="])"
        return string
    def push(self,num):
        self.stk.append(num)
    def pop(self):
        if(not self.empty()):
            a=self.stk.pop()
            return a
        else: 
            return None
    def top(self):
        if(not self.empty()): return self.stk.get(self.stk.size-1)
        else: return None
    def empty(self):
        return True if self.stk.size==0 else False
    def clear(self):
        self.stk.clear()
            

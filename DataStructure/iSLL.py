class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return f"Node({self.data})"
class SLL:
    def __init__(self,arr=[]):
        if not isinstance(arr,list) :
           raise ValueError("Initial input must be a list, or no input.")

        self.head=None
        self.tail=None
        self.size=0
        for i in arr:
            self.append(i)

    def __str__(self):#O(n)
        string="SLL(["
        curr=self.head
        while(curr!=None):
            string+=str(curr.data)+", "
            curr=curr.next
        if(self.size!=0):
            string=string[:-2]
        string+="])"
        return string

    def empty(self):#O(1)
        if(self.size==0):
            return True
        else:
            return False
    
    def append(self,sample):#O(1)
        if(self.empty()):
            self.head=Node(sample)
            self.tail=self.head
            self.size+=1
        else:
            self.tail.next=Node(sample)
            self.tail=self.tail.next
            self.size+=1

    def pop(self):
        if self.empty():
            return None
        elif self.size > 1:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            temp = self.tail
            a = temp.data
            self.tail = curr
            curr.next = None  # Set the next of the new tail to None
            self.size -= 1
            return a
        else:  # self.size == 1
            a = self.tail.data
            self.head = None
            self.tail = None
            self.size -= 1
            return a

    
    def clear(self):#O(n)
        if self.empty():
            return
        nxt=self.head.next
        while self.size>0:
            temp=self.head
            self.head=nxt
            if(nxt!=None):
                nxt=nxt.next
            temp.next=None
            self.size-=1

    
    def count(self, sample):#O(n)
        counter = 0
        curr=self.head
        while(curr is not None):
            if curr.data == sample:
                counter+=1
            curr=curr.next
        return counter
    
    def getNode(self,idx):#O(n)
        if self.empty():
            return None
        curr=self.head
        if not isinstance(idx, int):
            return None
        elif idx >= self.size:
            return self.tail
        elif idx<0:
            if abs(idx)>= self.size:
                return self.head
            else:
                return self.getNode(self.size+idx)
        else:
            for x in range(0,idx):
                curr=curr.next
        return curr
            
    def get(self,idx):#O(1)
        if self.empty():
            return None
        else:
            return self.getNode(idx).data
    
    def copy(self):#O(n)
        if self.empty():
            return SLL()
        arr=[]
        curr=self.head
        while curr != None:
            arr.append(curr.data)
            curr=curr.next
        return SLL(arr)

    def extend(self, samplesll):#O(1)
        if not isinstance(samplesll, SLL):
            return
        elif self.empty() and not samplesll.empty():
            self=samplesll
            return
        elif not self.empty() and samplesll.empty():
            return 
        elif self.empty() and samplesll.empty():
            return
        else:
            self.tail.next = samplesll.head
            self.size += samplesll.size
            self.tail = samplesll.tail

    def index(self, sample):#O(n)
        if self.empty():
            return None 
        else:
            idx=0
            curr=self.head
            while(curr!=None):
                if(curr.data==sample):
                    return idx
                else:
                    idx+=1
                curr=curr.next
            return None
    
    def insert(self,idx,sample):#O(1)
        if self.empty():
            self.append(sample)
        elif abs(idx)>=self.size:
            if idx>=self.size:
                self.append(sample)
            else:
                temp=Node(sample)
                temp.next=self.head
                self.size+=1
                self.head=temp
        elif idx>0:
            temp1=Node(sample)
            curr=self.getNode(idx-1)
            temp2=curr.next
            curr.next=temp1
            temp1.next=temp2
            self.size+=1
        elif idx==0:
            temp=Node(sample)
            temp.next=self.head
            self.size+=1
            self.head=temp
        else:
            idx=self.size+idx
            self.insert(idx, sample)

    def reverse(self):#O(n)
        if self.empty() or self.size==1:
            return
        else:
            prev=None
            curr=self.head
            nxt=self.head.next
            temp1=self.tail
            while curr!=None:
                curr.next=prev
                prev=curr
                curr=nxt
                if nxt!=None:
                    nxt=nxt.next
            self.tail=self.head
            self.head=temp1
            return
                
            
            
            

        

            
            
        

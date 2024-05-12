arr=[]
arr.

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class SLL:
    def __init__(self,arr=[]):
        self.head=None
        self.tail=None
        self.size=0
        for i in arr:
            self.append(i)

    def append(self,data):
        temp=Node(data)
        if(self.head==None):
            self.head=temp
            self.tail=temp
            self.size+=1
        else:
            self.tail.next=temp
            self.tail=self.tail.next
            self.size+=1

    def clear(self):
        while(self.size!=0):
            self.pop()

    def copy(self):
        new_sll=SLL()
        curr=self.head
        while(curr!=None):
            new_sll.append(curr.data)
            curr=curr.next
        return new_sll

    def count(self,sample):
        curr=self.head
        cnt=0
        while(curr!=None):
            if(curr.data==sample):
                cnt+=1
            curr=curr.next
        return cnt

    def extend(self,e_SLL):
        if not isinstance(e_SLL,SLL):
            return
        if(self.head.data==None):
            self.head=e_SLL.head
            self.tail=e_SLL.tail
            self.size=e_SLL.size
            return
        self.tail.next=e_SLL.head
        if(e_SLL.tail.data!=None):
            self.tail=e_SLL.tail
        self.size+=e_SLL.size
        
    def index(self,sample):
        idx=None
        i=0
        curr=self.head
        while(curr!=None):
            if(curr.data==sample):
                idx=i
                return idx
            i+=1
            curr=curr.next
        return idx
        
    def insert(self,smp_idx,sample):
        if(smp_idx>=0):
            if(smp_idx>=self.size):
                self.append(sample)
            else:
                temp=Node(sample)
                if(smp_idx==0):
                    temp.next=self.head
                    self.head=temp
                    self.size+=1
                    return
                curr=self.head
                for i in range(0,smp_idx-1):
                    curr=curr.next
                temp.next=curr.next
                curr.next=temp
                self.size+=1
                return
        else:
            if(abs(smp_idx)>=self.size):
                temp=Node(sample)
                temp.next=self.head
                self.head=temp
                self.size+=1
                return
            else:
                self.insert(self.size+smp_idx,sample)

    def pop(self):
        if self.head==None:
            return None
        curr=self.head
        while(curr.next!=self.tail):
            curr=curr.next
        temp=self.tail
        self.tail=curr
        a=temp.data
        del temp
        self.size-=1
        return a

    def remove(self,sample):
        if(self.size==0):
            return
        curr=self.head
        if(curr.data==sample):



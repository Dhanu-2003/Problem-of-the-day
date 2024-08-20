class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.temp = 0
    def create(self,data = []):
        if type(data) is int or type(data) is float:
            self.insertAtEnd(data)
        if type(data) is list or type(data) is tuple:
            for i in data:
                self.insertAtEnd(i)
        
    def insertAtBegining(self,data):
        new = Node(data)
        if self.head==None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new
        self.size+=1
    def insertAtEnd(self,data):
        new = Node(data)
        if self.head==None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.size+=1
    def insertAtIndex(self,ind,data):
        self.temp = 0
        tptr = self.head
        if ind==0:
            self.insertAtBegining(data)
            return
        while tptr.next!=None and self.temp<ind-1:
            tptr = tptr.next
            self.temp+=1
        new = Node(data)
        new.next = tptr.next
        tptr.next = new
        self.size+=1

    def valueAt(self,ind):
        tptr = self.head
        self.temp = 0
        while tptr!=None and self.temp<ind:
            tptr=tptr.next
            self.temp+=1
        if tptr!=None:
            return tptr.data
        else:
            return None
    def slice(self,start,end, rev = 1):
        tptr = self.head
        self.temp = 0
        while tptr!=None and self.temp<start:
            tptr = tptr.next
            self.temp += 1
        temp_linked = LinkedList()
    
        for i in range(end-start):
            temp_linked.insertAtEnd(tptr.data)
            tptr = tptr.next
            if tptr==None:
                break
        if rev==-1:
            temp_linked.reverse()
        return temp_linked
    
    def reverse(self):
        pre = None
        cur = None
        nex = self.head
        while nex!=None:
            cur = nex
            nex = nex.next
            cur.next = pre
            pre = cur
        self.head = cur
    def get(self,ind = 0):
        tptr = self.head
        self.temp = 0
        if ind!=0:
            while tptr.next!=None and self.temp<ind-1:
                tptr = tptr.next
                self.temp+=1
            if self.temp==ind-1 and tptr.next!=None:
                temp_data = tptr.next.data
                tptr.next = tptr.next.next 
              
            else:
                return 
        else:
            temp_data = tptr.data 
            self.head = tptr.next  
        self.size-=1
        return temp_data
    
    def remove(self,ind=0):
        tptr = self.head
        self.temp = 0
        if ind==0:
            self.head = tptr.next
        else:
            while tptr.next!=None and self.temp<ind-1:
                tptr = tptr.next
                self.temp+=1
            if tptr.next!= None:
                tptr.next = tptr.next.next
            else:
                return
        self.size-=1
    def find(self,data):
        tptr = self.head
        self.temp = 0
        while tptr!=None:
            if(tptr.data==data):
                return self.temp
            self.temp+=1
            tptr = tptr.next
    def findAll(self,data):
        ind_list = []
        self.temp = 0
        tptr = self.head
        while tptr!=None:
            if tptr.data==data:
                ind_list.append(self.temp)
            self.temp+=1
            tptr = tptr.next
        return ind_list
    
    def dataFreq(self):
        freq = {}
        tptr = self.head
        while tptr!=None:
            if tptr.data in freq:
                freq[tptr.data]+=1
            else:
                freq[tptr.data] = 1
            tptr = tptr.next
        return freq
    def copy(self):
        obj = LinkedList()
        tptr = self.head
        while tptr!=None:
            obj.insertAtEnd(tptr.data)
            tptr = tptr.next
        return obj
    
    def count(self,data):
        count = 0
        tptr = self.head
        while tptr!=None:
            if tptr.data==data:
                count+=1
            tptr = tptr.next
        return count
    
    def Unique(self):
        data = self.dataFreq()
        obj = LinkedList()
        for i in data:
            obj.insertAtEnd(i)

        return obj
    
    
    def show(self):
        tptr = self.head
        if tptr==None:
            print(self.head)
            return
        while tptr.next!=None:
            print(tptr.data,end = "->")
            tptr = tptr.next
        print(tptr.data)


obj = LinkedList()

obj.insertAtEnd(10)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(15)
obj.insertAtEnd(7)
obj.insertAtEnd(9)
obj.insertAtEnd(20)
obj.insertAtEnd(37)

obj.show()
obj.insertAtIndex(7,100)
obj.show()

x = obj.slice(2,8)
x.show()
x.reverse()
x.show()

x.remove()
x.show()
print(x.get(1))
x.show()

print(x.valueAt(3))
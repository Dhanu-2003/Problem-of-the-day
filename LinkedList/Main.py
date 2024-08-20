from LinkedList import *
print()
print()


l1 = LinkedList()

l1.create([1,2,3,4,5]) #tested with integer and tuple and list


l1.insertAtBegining(10)
l1.insertAtBegining(20) # tested

l1.insertAtEnd(30)
l1.insertAtEnd(5)   #tested

l1.insertAtIndex(20,400) #tested
l1.show()
l1.insertAtIndex(6,300)
l1.show()

print(l1.valueAt(l1.size-1)) #tested

l1.show()
temp = l1.slice(3,6,-1)  #testes
temp.show()

temp.reverse() #tested
temp.show()


l1.show()
print(l1.get()) #tested
l1.show()

l1.show()
print(l1.size)
l1.remove() #tested  
l1.show()

print(l1.find(4)) #tested

print(l1.findAll(5))   #tested

print(l1.dataFreq()) #tested
 
cop = l1.copy()  #tested

cop.show()

print(cop.count(1))  #tested

cop.Unique().show()  #tested

import time
import random



#TESTING LIST, TUPLE, LINKEDLIST
print("___________TEST__________________")

print()
print("CREATION")
print()

t1 = round(time.time(),1)
a1 = [random.randint(1324,90290239208) for i  in range(10000000)]
t2 = round(time.time(),1)
Lt = t2-t1
print((Lt))


t1 = round(time.time(),1)
a2 = LinkedList()
for i in range(10000000):
    a2.insertAtEnd(random.randint(1324,90290239208))
t2 = round(time.time(),1)
Lt = t2-t1
print(Lt)



print()
print("getting value")
print()

t1 = round(time.time(),1)
print(a1[len(a1)-1])
t2 = round(time.time(),1)
Lt = t2-t1
print(Lt)


t1 = round(time.time(),1)
a2.valueAt(a2.size-1)
t2 = round(time.time(),1)
Lt = t2-t1
print(Lt)

print(a1.count(a1[-1]))
print()
print("deleting value")
print()

t1 = time.time()
a1.remove(a1[1])
t2 = time.time()
Lt = t2-t1
print(Lt)


t1 = time.time()
a2.remove(1)
t2 = time.time()
Lt = t2-t1
print(Lt)




print()
print("insertion")
print()

t1 = time.time()
a1.insert(1,43534535)
t2 = time.time()
Lt = t2-t1
print((Lt))

t1 = time.time()
a2.insertAtIndex(1,43534535)
t2 = time.time()
Lt = t2-t1
print((Lt))


print()
print("unique")
print()

t1 = time.time()
x = set(a1)
t2 = time.time()
Lt = t2-t1
print((Lt))

t1 = time.time()
a2.Unique()
t2 = time.time()
Lt = t2-t1
print((Lt))

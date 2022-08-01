#priority queue using normal queue and sort method

#Here we will sort the value in any order to represent it as proirity and then pop it
queue=[]
queue.append(90)
queue.sort()
queue.append(20)
queue.sort()
queue.append(70)
queue.sort()

print(queue)


#Priority queue using priority queue using class
import queue

q=queue.PriorityQueue()
#To add element
q.put(10)
q.put(60)
q.put(20)
q.put(40)

#To remove element based on priority

q.get()
q.get()
q.get()

print(q.get())


#We can also use tuple
import queue
q=[]
q.append((9,"aswin"))
q.append((14,"ash"))
q.append((8,"anu"))
q.sort() # sorting it
#removing it as per priority

x=q.pop(0)
print(q)
print("removed item is ",x)
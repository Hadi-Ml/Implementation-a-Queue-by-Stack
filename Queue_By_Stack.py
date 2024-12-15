class Queue :
    def __init__(self):
        self.Queue1 = []
        self.Queue2 = []

    def enqueue(self, value):
        self.Queue1 += [value]
        return self.Queue1

    def dequeue(self):
        counter1 = 0
        counter2 = 0
        for i in self.Queue1:
            counter1 += 1
        for i in self.Queue2:
            counter2 += 1

        if counter1 != 0 or counter2 != 0:
            if counter2 == 0 :
                for i in range (counter1-1,-1,-1):
                    self.Queue2 += [self.Queue1[i]]
                self.Queue1 = []
                removed_value = self.Queue2[-1]
                self.Queue2 = self.Queue2 [0:-1]
                return removed_value , self.Queue2

            else : #self.counter2 != 0
                removed_value = self.Queue2[-1]
                self.Queue2 = self.Queue2 [0:-1]
                return removed_value , self.Queue2
        else :
            return "Queue is Empty"




#-----------------------------------------------------------------------------------------------------------------------

q = Queue()

print("\n")

print(q.enqueue(100),"\n")
print(q.enqueue(200),"\n")
print(q.enqueue(300),"\n")
print(q.enqueue(400),"\n")
print(q.enqueue(500),"\n")

print(q.dequeue(),"\n")
print(q.dequeue(),"\n")
print(q.dequeue(),"\n")
print(q.dequeue(),"\n")
print(q.dequeue(),"\n")
print(q.dequeue(),"\n")

print(q.enqueue(80),"\n")
print(q.enqueue(70),"\n")

print(q.dequeue(),"\n")
print(q.dequeue(),"\n")
print(q.dequeue(),"\n")






from random import random
class Animal:
    def __init__(self, type, next=None)-> None:
        self.type = type 
        self.next = next
    def __str__(self):
        return self.type
class ShelterQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
    def __str__(self):
        values = [str(val) for val in self]
        return ("->").join(values)
    def enqueue(self, value):
        animal = Animal(value)
        if self.head==None:
            self.head = self.tail = animal
        else:
            animal.next = self.head
            self.head = animal
    def dequeueAny(self):
        if self.head==None:
            print("Shelter is empty\n")
            return None
        animal = self.head
        self.head = self.head.next
        return animal
    def dequeueAnimal(self, type="Cat"):
        animal = self.head
        # Queue has nonodes
        if animal is None:
            print("Shelter is empty\n")
            return 
        while animal:
            #  First animal node is of interest
            if animal.type[:3]==type:
                self.head= self.head.next
                return animal
            # Queue with just one node 
            if animal.next is None:
                if animal.type[:3]==type:
                    self.head = self.tail =None
                    return animal
            # All other cases 
            elif animal.next.type[:3]==type:
                res = animal.next
                animal.next = animal.next.next
                res.next = None
                return res
            animal = animal.next
        return None
    def generate(self, n):
        for num in range(1, n+1):
            value = ("Dog" if random() >0.5 else "Cat")+str(num)
            # print(value[3:])
            self.enqueue(value)
    # def 

shelterq = ShelterQueue()
shelterq.generate(10)
print(shelterq)
print(shelterq.dequeueAnimal())
print(shelterq)
print(shelterq.dequeueAnimal())
print(shelterq)
print(shelterq.dequeueAnimal())
print(shelterq)
print(shelterq.dequeueAnimal())
print(shelterq)
print(shelterq.dequeueAnimal())
print(shelterq)
print(shelterq.dequeueAnimal())
print(shelterq)
print(shelterq.dequeueAnimal("Dog"))
print(shelterq)
print(shelterq.dequeueAnimal("Dog"))
print(shelterq)
print(shelterq.dequeueAnimal("Dog"))
print(shelterq)
print(shelterq.dequeueAnimal("Dog"))
print(shelterq)
print(shelterq.dequeueAnimal("Dog"))
print(shelterq)
print(shelterq.dequeueAnimal("Dog"))
print(shelterq)
# print(shelterq.dequeueAnimal())
# print(shelterq)
# print(shelterq.dequeueAnimal())
# print(shelterq)
# print(shelterq.dequeueAnimal())
# # print(shelterq.dequeueAny())
# # print(shelterq)
# # print(shelterq.dequeueAny())
# # print(shelterq)
# # print(shelterq.dequeueAny())
# # print(shelterq)
# print(shelterq.dequeueAny())
# print(shelterq)
# print(shelterq.dequeueAny())
# print(shelterq)
# print(shelterq.dequeueAny())
# print(shelterq)
# print(shelterq.dequeueAny())
# print(shelterq)
# print(shelterq.dequeueAny())
# print(shelterq)
# print(shelterq.dequeueAny())
# print(shelterq)
# print(shelterq.dequeueAny())
# print(shelterq)
# print(shelterq.dequeueAny())
# print(shelterq)
            


    
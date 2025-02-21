# [this is a good song](https://youtu.be/VYXsP_dosuk?si=hGv8yg4vxrbuRkVk)

N, K = map(int, input().split())

# this was really annoying I had alot  of random bugs, so I had to pull out the classes
#I had a lot of random bugs, which luckily I was able to fix
# I did have to generate some random ext cases with this script

# ```py
# import random
# import sys

# sys.stdout = open("01.in", "w")


# N = 100
# K = 1000

# print(N,K)

# for _ in range(N):
#     type = random.choice(["NZ", "DIP", "IT"])
#     name = _ + 1
#     print(type, name)
# for _ in range(K):
#     print(random.choice(["NZ", "DIP", "IT"]))`

# ALSO the command like is really cool cause like why can u just go 

# > python .\gen_cases.py 
# > more 01.in | python '.\Passport Control.py'

# like isn't that so broken?


class Node:
    # grrr i had to pull out the classes this is really sad
    def __init__(
        self,
        name,
        previous,
        next,
        special_previous=None,
        special_next=None,
    ):
        self.name = name
        self.previous = previous
        self.next = next
        self.special_previous = special_previous
        self.special_next = special_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nz_head = None
        self.nz_tail = None
        self.dip_head = None
        self.dip_tail = None

    def append(self, name, type="ALL"):
        new_node = Node(name, None, None)
        # everything adds to the main queue
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        if type == "NZ":
            if self.nz_head is None:
                self.nz_head = new_node
                self.nz_tail = new_node
            else:
                new_node.special_previous = self.nz_tail
                self.nz_tail.special_next = new_node
                self.nz_tail = new_node
        elif type == "DIP":
            if self.dip_head is None:
                self.dip_head = new_node
                self.dip_tail = new_node
            else:
                new_node.special_previous = self.dip_tail
                self.dip_tail.special_next = new_node
                self.dip_tail = new_node

    def display(self):
        print("Main Queue: ")
        current = self.head
        while current:
            print(" ", current.name)
            current = current.next
        print()
        print("NZ Queue: ")
        current = self.nz_head
        while current:
            print(" ", current.name)
            current = current.special_next
        print()
        print("Diplomat Queue: ")
        current = self.dip_head
        while current:
            print(" ", current.name)
            current = current.special_next
        print()

    def pop(self, type="ALL"):
        if type == "ALL":
            if self.head is None:
                return "NA"
            else:
                name = self.head.name
                if self.head is self.nz_head:
                    self.nz_head = self.nz_head.special_next
                elif self.head is self.dip_head:
                    self.dip_head = self.dip_head.special_next
                elif self.head.special_previous:
                    self.head.special_previous.special_next = self.head.special_next
                    if self.head.special_next:
                        self.head.special_next.special_previous = (
                            self.head.special_previous
                        )
                self.head = self.head.next
                return name
        if type == "NZ":
            if self.nz_head is None:
                return "NA"
            else:
                name = self.nz_head.name
                if self.head is self.nz_head:
                    self.head = self.head.next
                else:
                    self.nz_head.previous.next = self.nz_head.next
                    if self.nz_head.next is not None:
                        self.nz_head.next.previous = self.nz_head.previous
                self.nz_head = self.nz_head.special_next
                return name
        if type == "DIP":
            if self.dip_head is None:
                return "NA"
            else:
                name = self.dip_head.name
                if self.head is self.dip_head:
                    self.head = self.head.next
                else:
                    self.dip_head.previous.next = self.dip_head.next
                    if self.dip_head.next is not None:
                        self.dip_head.next.previous = self.dip_head.previous
                self.dip_head = self.dip_head.special_next
                return name


queue = LinkedList()

for i in range(N):
    type, name = input().split()
    queue.append(name, type)

# queue.display()
for i in range(K):
    # queue.display()
    print(queue.pop(input()))
    # print(f"popped {queue.pop(input())} \n")
    # queue.display()

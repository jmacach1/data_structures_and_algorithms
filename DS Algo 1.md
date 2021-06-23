```python
print("Hello World")
```

    Hello World


# Problem 1

### Given two strings (string_a and string_b) let's check whether or not they are anagrams of each other given the following criteria:
> Two strings are only anagrams of each other if all conditions below are met:
> * They must be exactly the same length.
> * They must use exactly the same characters (no more, no less)

Example: cars and scar, heart and earth, etc.

----
Use a dictionary with the letter as the key and the number_of_times used. 
Go through each string and count each

special characters - spaces, apostrophes, hyphen
Uppercase and lowercase - 


```python
def is_anagram(string_a, string_b):
    if len(string_a) is not len(string_b):
        return False
    
    char_times_a = dict()
    char_times_b = dict()
    
    for i in range(len(string_a)):
        if string_a[i] not in char_times_a.keys():
            char_times_a[string_a[i]] = 0
        else:
            char_times_a[string_a[i]] += 1
            
        if string_b[i] not in char_times_b.keys():
            char_times_b[string_b[i]] = 0
        else:
            char_times_b[string_b[i]] += 1
    return char_times_a == char_times_b
```


```python
is_anagram("cars", "scar")
```




    True




```python
is_anagram("sccr", "scar")
```




    False




```python
is_anagram("I am lord Voldemort", "Tom Marvolo Riddle")
```




    False




```python
def createLetterDict(string_a):
    char_times = dict()
    for letter in string_a:
        if letter == " ":
            continue
        letter = letter.lower()
        if letter not in char_times:
            char_times[letter] = 1
        else:
            char_times[letter] += 1

def is_anagram2(string_a, string_b):
    if len(string_a) == len(string_b):
        return False
    
    char_times_a = createLetterDict(string_a)
    char_times_b = createLetterDict(string_b)
    return char_times_a == char_times_b
```


```python
is_anagram2("I am lord Voldemort", "Tom Marvolo Riddle")
```




    True




```python
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
```


```python
def reverse_str(s):
    stack = Stack()
    # iterate and push to stack
    for char in s:
        stack.push(char)
    
    # while stack is not empty pop and append to list    
    collector = ""
    while not stack.is_empty():
        collector += stack.pop()
        
    print(collector)
    return collector
```


```python
def test_reverse_str():
    assert reverse_str("racecar") == "racecar"
    assert reverse_str("SDGKU") == "UKGDS"
    assert reverse_str("ping pong") == "gnop gnip"
```


```python
test_reverse_str()
```

    racecar
    UKGDS
    gnop gnip



```python
class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
        
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]
    
    def size(self):
        return len(self.items)
```


```python
def test_queue():
    queue = Queue()
    queue.push("A")
    queue.push("C")
    queue.push("E")
    print("A == " + queue.pop())
    print("C == " + queue.pop())
    print("E == " + queue.pop())
    print("None == " + str(queue.pop()))

```


```python
test_queue()
```

    A == A
    C == C
    E == E
    None == None



```python
from string import ascii_lowercase
from random import randint, choice
from time import sleep

def register_visitor(visitor_queue):
    for char in ascii_lowercase:
        visitor_queue.push(char)
    
def service_customers(visitor_queue):
    bank_tellers = ["A", 'B', 'C', 'D', 'E', 'F', 'G']
    while not visitor_queue.is_empty():
        visitor = visitor_queue.pop()
        print(f"Thank you for waiting {visitor}, station {choice(bank_tellers)} is ready for you.")
        sleep(randint(1,2))
    print("Empty visitor queue.")
    
def main():
    visistor_queue = Queue()
    register_visitor(visistor_queue)
    service_customers(visistor_queue)                     
```


```python
main()
```

    Thank you for waiting a, station A is ready for you.
    Thank you for waiting b, station A is ready for you.
    Thank you for waiting c, station D is ready for you.
    Thank you for waiting d, station G is ready for you.
    Thank you for waiting e, station A is ready for you.
    Thank you for waiting f, station E is ready for you.
    Thank you for waiting g, station F is ready for you.
    Thank you for waiting h, station C is ready for you.
    Thank you for waiting i, station E is ready for you.
    Thank you for waiting j, station G is ready for you.
    Thank you for waiting k, station F is ready for you.
    Thank you for waiting l, station E is ready for you.
    Thank you for waiting m, station G is ready for you.
    Thank you for waiting n, station A is ready for you.
    Thank you for waiting o, station G is ready for you.
    Thank you for waiting p, station D is ready for you.
    Thank you for waiting q, station G is ready for you.
    Thank you for waiting r, station G is ready for you.
    Thank you for waiting s, station B is ready for you.
    Thank you for waiting t, station B is ready for you.
    Thank you for waiting u, station A is ready for you.
    Thank you for waiting v, station C is ready for you.
    Thank you for waiting w, station C is ready for you.
    Thank you for waiting x, station B is ready for you.
    Thank you for waiting y, station A is ready for you.
    Thank you for waiting z, station C is ready for you.
    Empty visitor queue.



```python
# Assignment 1
# Balanced parentheses check

def balance_check(s):
    if (len(s) % 2 != 0): # if odd, return False
        return False
    
    stack = Stack()
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    pairs = dict()
    for i in range(len(opening)):
        pairs[closing[i]] = opening[i]
    
    # iterate through s with char
    for char in s: 
        
        # if char is opening, add to stack
        if char in opening: 
            stack.push(char)
            
        # if car is closing 
        elif char in closing:
            
            # pop the last_opening
            last_opening = stack.pop() 
            
            # if last_opening not complement of char return false
            if pairs[char] != last_opening: 
                return False


    # return true if stack is empty
    return stack.is_empty()

# def balance_check_2(s):
#     if (len(s) % 2 != 0):
#         return False
    
#     opening = ['(', '[', '{']
#     closing = [')', ']', '}']
#     pairs = dict()
#     for i in range(len(opening)):
#         pairs[closing[i]] = opening[i]
    
#     stack = Stack()
#     for char in s:
#         if char in opening: 
#             stack.push(char)
#         elif char in closing:
#             last_opening = stack.pop()
#             if pairs[char] != last_opening: 
#                 return False
#     return stack.is_empty()
```


```python
assert balance_check("Hellow") == True

assert balance_check("()") == True
assert balance_check("(") == False

assert balance_check("(){}[]{}()") == True
assert balance_check("){}[]{}()") == False

assert balance_check("{}[()]{()}") == True
assert balance_check("{}[()]{()}(") == False

assert balance_check("((((((((((((((()))))))))))))))") == True
assert balance_check("((((((((((((((()))))))))])))))") == False
```


```python
# replace

def replace(string, target, replacement):
    splitString = list(string)
    for i in range(len(splitString)):
#         print(f"{i} {splitString[i]}")
        if splitString[i] == target:
            splitString[i] = replacement
    return "".join(splitString)
            
```


```python
assert replace("AAABBBAAA", "A", "Z") == "ZZZBBBZZZ"
# print(replace("AAABBBAAA", "A", "Z"))
```


```python
# Assignment 2
class Queue2Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, element):
        self.stack1.append(element)
    
    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        
        if len(self.stack2):
            return self.stack2.pop()
            
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
            
        return self.stack2.pop()
```


```python
def test_Queue2Stacks():
    q = Queue2Stacks()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())
```


```python
test_Queue2Stacks()
```

    0
    1
    2
    3
    4



```python
def rec_factorial(n):
    if n == 1:
        return 1
    return n * rec_factorial(n - 1)
```


```python
rec_factorial(6)
```




    720




```python
# memo = {
#     0 : 0,
#     1 : 1
# }
# def fib(n):
#     if n in memo:
#         return memo[n]
#     result = fib(n - 1) + fib(n - 2)
#     memo[n] = result
#     return result

from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```


```python
for i in range(10):
    print(f"fib({i}) {fib(i)}")
```

    fib(0) 0
    fib(1) 1
    fib(2) 1
    fib(3) 2
    fib(4) 3
    fib(5) 5
    fib(6) 8
    fib(7) 13
    fib(8) 21
    fib(9) 34



```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```


```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
            
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        
    def insert_after(self, target, data):
        if self.head is None:
            raise Exception("No head")
        
        new_node = Node(data)
        beforeNode = self.head
        while beforeNode and beforeNode.data != target:
            beforeNode = beforeNode.next
        
        if not beforeNode:
            raise ValueError("Unable to find target")
            
        new_node.next = beforeNode.next
        beforeNode.next = new_node
        
        if self.tail is beforeNode:
            self.tail = beforeNode.next
        
    
    def remove(self, target):
        if self.head is None:
            raise Exception("No list")
            
        if self.head.data == target:
            self.head = self.head.next
            return
        
        pointer = self.head
        while pointer.next and pointer.next.data != target:
            pointer = pointer.next
            
        if not pointer.next:
            raise ValueError("Unable to find target")
            
        if pointer.next == self.tail:
            self.tail = pointer
        pointer.next = pointer.next.next
            
    
    def print(self):
        printStatement = list()
        printStatement.append(f"self.head => {self.head.data} \n")
        printStatement.append(f"self.tail => {self.tail.data} \n")
        
        pointer = self.head
        while pointer:
            printStatement.append(f"{pointer.data}")
            printStatement.append(" -> ")
            pointer = pointer.next
    
        print("".join(printStatement))
        
    def index_of(self, target):
        if not self.head:
            raise ValueError("No list")
        
        count = 0
        pointer = self.head
        while pointer and pointer.data != target:
            count += 1
            pointer = pointer.next
    
        if not pointer:
            raise ValueError("Target not found")
            
        return count
    
    def max(self):
        if not self.head:
            raise ValueError("No max. No List")
            
        pointer = self.head
        max = self.head.data
        while pointer:
            if (pointer.data > max):
                max = pointer.data
            pointer = pointer.next

                
        return max
        
```


```python
linkedList = LinkedList()
print("\nLinkedList")
linkedList.append(4)
linkedList.print()

print("\nPrepending 3, 2")
linkedList.prepend(3)
linkedList.prepend(2)
linkedList.print()

print("\nAppending 8, 9")
linkedList.append(8)
linkedList.append(9)
linkedList.print()

print("\nInserting 6 after 4, 5 after 4, 7 after 6")
linkedList.insert_after(4,6)
linkedList.insert_after(4,5)
linkedList.insert_after(6,7)
linkedList.print()

print("\n testing index_of ")
print(f"2 is in index {linkedList.index_of(2)}")
print(f"4 is in index {linkedList.index_of(4)}")
print(f"6 is in index {linkedList.index_of(6)}")
print(f"9 is in index {linkedList.index_of(9)}")

print("\nRemoving the Head - 2, 3")
linkedList.remove(2)
linkedList.remove(3)
linkedList.print()

print("\nRemoving the Tail 9, 8")
# removing the tail
linkedList.remove(9)
linkedList.remove(8)
linkedList.print()

print("\nRemoving the Middle 5, 6")
linkedList.remove(6)
linkedList.remove(5)
linkedList.print()

print("\nMax")
linkedList.print()
print(linkedList.max())
linkedList.append(19)
linkedList.print()
print(linkedList.max())
linkedList.prepend(20)
linkedList.print()
print(linkedList.max())
linkedList.insert_after(4,21)
linkedList.print()
print(linkedList.max())
```

    
    LinkedList
    self.head => 4 
    self.tail => 4 
    4 -> 
    
    Prepending 3, 2
    self.head => 2 
    self.tail => 4 
    2 -> 3 -> 4 -> 
    
    Appending 8, 9
    self.head => 2 
    self.tail => 9 
    2 -> 3 -> 4 -> 8 -> 9 -> 
    
    Inserting 6 after 4, 5 after 4, 7 after 6
    self.head => 2 
    self.tail => 9 
    2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 
    
     testing index_of 
    2 is in index 0
    4 is in index 2
    6 is in index 4
    9 is in index 7
    
    Removing the Head - 2, 3
    self.head => 4 
    self.tail => 9 
    4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 
    
    Removing the Tail 9, 8
    self.head => 4 
    self.tail => 7 
    4 -> 5 -> 6 -> 7 -> 
    
    Removing the Middle 5, 6
    self.head => 4 
    self.tail => 7 
    4 -> 7 -> 
    
    Max
    self.head => 4 
    self.tail => 7 
    4 -> 7 -> 
    7
    self.head => 4 
    self.tail => 19 
    4 -> 7 -> 19 -> 
    19
    self.head => 20 
    self.tail => 19 
    20 -> 4 -> 7 -> 19 -> 
    20
    self.head => 20 
    self.tail => 19 
    20 -> 4 -> 21 -> 7 -> 19 -> 
    21



```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```


```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        new_node = DNode(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        if not self.tail:
            self.set_tail()
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def prepend(self, data):
        new_node = DNode(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
            
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        
    def set_tail():
        pointer = self.head
        if not pointer:
            raise ValueError("set_tail() - no self.head")
            
        while pointer.next:
            pointer = pointer.next
        self.tail = pointer
        
    def insert_after(self, target, data):
        target_node = self._search_target(target)
        if not target_node:
            raise ValueError(f"insert_after() - cannot find target : {target}")
        
        new_node = DNode(data)
        new_node.prev = target_node
        new_node.next = target_node.next
        
        target_node.next = new_node
        next_node = new_node.next
        if next_node:
            next_node.prev = new_node
        else:
            self.tail = new_node
    
    def insert_before(self, target, data):
        target_node = self._search_target(target)
        if not target_node:
            raise ValueError(f"insert_after() - cannot find target : {target}")
            
        new_node = DNode(data)
        new_node.next = target_node
        new_node.prev = target_node.prev
        
        target_node.prev = new_node
        prev_node = new_node.prev
        if prev_node:
            prev_node.next = new_node
        else:
            self.head = new_node
            
    
    def remove(self, target):
        target_node = self._search_target(target)
        if not target_node:
            raise ValueError(f"remove() - cannot find target : {target}")
        
        if target_node is self.head:
            self.head = self.head.next
        
        if target_node is self.tail:
            self.tail = self.tail.prev
        
        prev_node = target_node.prev
        next_node = target_node.next
        
        if prev_node:
            prev_node.next = target_node.next
            
        if next_node:
            next_node.prev = target_node.prev
        
    def _search_target(self, target):

        pointer = self.head
        while pointer:
            if pointer.data == target:
                return pointer
            pointer = pointer.next
            
        return None
            
    
    def index_of(self, target):
        pointer = self.head
        counter = 0
        while pointer and pointer.data != target:
            pointer = pointer.next
            counter += 1
        if not pointer:
            raise ValueError("index_of(target) - target not found")
        return counter
        
    
    def maximum(self):
        if not self.head:
            raise ValueError("maximum() - No head")
        
        pointer = self.head
        maximum = pointer.data
        while pointer:
            if (pointer.data > maximum):
                maximum = pointer.data
            pointer = pointer.next
                
        return maximum
    
    def minimum(self):
        if not self.head:
            raise ValueError("minimum() - No head")
            
        pointer = self.head
        minimum = pointer.data
        while pointer:
            if (pointer.data < minimum):
                minimum = pointer.data
            pointer = pointer.next
            
        return minimum
    
        
    def mode(self):
        if not self.head:
            raise ValueError("mode() - No head")
        
        num_dict = dict()
        pointer = self.head
        while pointer:
            if pointer.data not in num_dict: 
                num_dict[pointer.data] = 0
            num_dict[pointer.data] += 1
            pointer = pointer.next
        
        highestCount = 0
        highestNum = ""
        for key, value in num_dict.items():
            if value > highestCount:
                highestCount = value
                highestNum = key
        
        return highestNum
        
    
    def median(self):
        if not self.head:
            raise ValueError("mode() - No head")
        
        dataList = list()
        pointer = self.head
        while pointer:
            dataList.append(pointer.data)
            pointer = pointer.next
        
        dataList.sort()
        half = len(dataList) // 2 
        if len(dataList) % 2 == 0:
            return (dataList[half - 1] + dataList[half]) / 2 
        return dataList[half]
        
    
    def mean(self):
        if not self.head:
            raise ValueError("mean() - No head")
        
        total = 0
        counter = 0
        pointer = self.head
        while pointer:
            counter += 1
            total += pointer.data
            pointer = pointer.next
            
        return total / counter
            
        
    
    def printList(self):
        print("{")
        indent = "  "
        print(f"{indent}self.head : {self.head.data if self.head else None}")
        print(f"{indent}self.tail : {self.tail.data if self.tail else None}")
        
        
        pointer = self.head
        print(f"{indent}Nodes : ")
        indent = indent * 2
        while pointer:
            prev = pointer.prev.data if pointer.prev else None
            next = pointer.next.data if pointer.next else None
            print(f"{indent}prev={prev} data={pointer.data} next={next}")
            pointer = pointer.next
    
        print("}")
        
    def __len__(self):
        pointer = self.head
        counter = 0
        while pointer:
            counter += 1
            pointer = pointer.next
            
        return counter
```


```python
dataPoints = {
    11 : 11,
    50 : 50,
    100 : 100,
    600 : 600,
    850 : 850,
    911 : 911
}

```


```python
linkedList = DoublyLinkedList()
print("Doubly Linked List")
print(f"Initial linkedList =>")
linkedList.printList()

print("Prepending 100, 50, 11 \n")
linkedList.prepend(dataPoints[100])
linkedList.prepend(dataPoints[50])
linkedList.prepend(dataPoints[11])
linkedList.printList()
```

    Doubly Linked List
    Initial linkedList =>
    {
      self.head : None
      self.tail : None
      Nodes : 
    }
    Prepending 100, 50, 11 
    
    {
      self.head : 11
      self.tail : 100
      Nodes : 
        prev=None data=11 next=50
        prev=11 data=50 next=100
        prev=50 data=100 next=None
    }



```python
print("Appending 600, 850, 911\n")
linkedList.append(dataPoints[600])
linkedList.append(dataPoints[850])
linkedList.append(dataPoints[911])
linkedList.printList()
```

    Appending 600, 850, 911
    
    {
      self.head : 11
      self.tail : 911
      Nodes : 
        prev=None data=11 next=50
        prev=11 data=50 next=100
        prev=50 data=100 next=600
        prev=100 data=600 next=850
        prev=600 data=850 next=911
        prev=850 data=911 next=None
    }



```python
print("index_of .......\n")

for key, value in dataPoints.items():
    print(f"index_of({value}) : {linkedList.index_of(value)}")
```

    index_of .......
    
    index_of(11) : 0
    index_of(50) : 1
    index_of(100) : 2
    index_of(600) : 3
    index_of(850) : 4
    index_of(911) : 5



```python
print("Removing 600, 100, 50\n")
linkedList.remove(dataPoints[600])
linkedList.remove(dataPoints[100])
linkedList.remove(dataPoints[50])
linkedList.printList()
```

    Removing 600, 100, 50
    
    {
      self.head : 11
      self.tail : 911
      Nodes : 
        prev=None data=11 next=850
        prev=11 data=850 next=911
        prev=850 data=911 next=None
    }



```python
print("insert_after(target,data) - (11, 50) (911, 1024) \n")
linkedList.insert_after(11,50)
linkedList.insert_after(911,1024)
linkedList.printList()
```

    insert_after(target,data) - (11, 50) (911, 1024) 
    
    {
      self.head : 11
      self.tail : 1024
      Nodes : 
        prev=None data=11 next=50
        prev=11 data=50 next=850
        prev=50 data=850 next=911
        prev=850 data=911 next=1024
        prev=911 data=1024 next=None
    }



```python
print("insert_before(target,data) - (11, 3) (850, 500) \n")
linkedList.insert_before(11,3)
linkedList.insert_before(850,500)
linkedList.insert_before(500,333)
linkedList.printList()
```

    insert_before(target,data) - (11, 3) (850, 500) 
    
    {
      self.head : 3
      self.tail : 1024
      Nodes : 
        prev=None data=3 next=11
        prev=3 data=11 next=50
        prev=11 data=50 next=333
        prev=50 data=333 next=500
        prev=333 data=500 next=850
        prev=500 data=850 next=911
        prev=850 data=911 next=1024
        prev=911 data=1024 next=None
    }



```python
print("mean .......")
linked_list_2 = DoublyLinkedList()
mode_num = 16
dataList = [39, mode_num, 8, 12, 22, 31, mode_num, 54, 48, mode_num, 37, 23, 31, 12, mode_num]


for data in dataList:
    linked_list_2.append(data)
    

print(f"maximum {linked_list_2.maximum()} == 54")
print(f"minimum {linked_list_2.minimum()} == 8")

print(f"mean {linked_list_2.mean()} == {sum(dataList) / len(dataList)}")
print(f"mode {linked_list_2.mode()} == {mode_num}")

dataList.sort()
print(f"median (odd) {linked_list_2.median()} == {dataList[len(dataList) // 2]}")

dataList.append(40)
linked_list_2.append(40)
half = len(dataList) // 2 
median_left = dataList[half - 1]
median_right = dataList[half]
print(f"median (even) {linked_list_2.median()} == {(median_left + median_right) / 2}")
```

    mean .......
    maximum 54 == 54
    minimum 8 == 8
    mean 25.4 == 25.4
    mode 16 == 16
    median (odd) 22 == 22
    median (even) 22.5 == 22.5



```python

```


```python

```

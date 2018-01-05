#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:21:13 2018

@author: hogwild
"""

class LinkedListUnderFlow(ValueError):
    pass


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        p = self._head
        n = 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderFlow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def insert(self, elem, i):
        if i == 0 or self._head is None:
            self.prepend(elem)
            return
        p = self._head
        while p is not None and i > 0:
            i -= 1
            p = p.next
        p.next = LNode(elem, p.next)

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end = "")
            if p.next is not None:
                print(',', end = "")
            p = p.next
        print('')

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter_(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p.next
            
    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p


class LListHT(LList):
    def __init__(self):
        super().__init__()
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)


    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear = LNode(elem, self._rear)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            self._rear = None
            return e
        while p.next.next is not None:
            p = p.next
        p.next = None
        e = self._rear.elem
        self._rear = p
        return e
    
    def rev(self):
        p = None
        self._rear = self._head
        self._rear.next = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p
        


class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
        self._rear = self._rear.next
               
    def pop(self):
        if self._rear is None:
            raise LinkedListUnderFlow("in pop")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderFlow("in pop_last")
        p = self._rear
        if self._rear is p:
            self._rear = None
            return p.elem
        while p.next is not self._rear:
            p = p.next
        e = p.next.elem
        p.next = self._rear.next
        self._rear = p
        return e

    def insert(self, elem, i):
        if self._rear is None:
            p = LNode(elem)
            p.next = p
            self._rear = p
            return
        elif i == 0:
            self._rear.next = LNode(elem, self._rear.next)
            return
        p = self._rear.next
        while i > 0:
            i -= 1
            if p is self._rear:
                break
            p = p.next
        p.next = LNode(elem, p.next)
        if p is self._rear:
            self._rear = p.next

    def length(self):
        p = self._rear.next
        n = 0
        while True:
            n += 1
            if p is self._rear:
                break
            p = p.next
        return n

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem, end = " ")
            if p is self._rear:
                break
            p = p.next
            
    def rev(self):
        p = self._rear
        rear = p.next
        if self._rear is None:
            return
        q = self._rear.next
        while True:
            temp = q.next
            q.next = p
            p = q
            if q is self._rear:
                break
            q = temp
        self._rear = rear
            

#### Double Linked List
class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        super().__init__(elem, next_)
        self.prev = prev
        

class DLListHT(LListHT):
    def __init__(self):
        super().__init__()
        
    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p
    
    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p
    
    def pop(self):
        if self._head is None:
            raise LinkedListUnderFlow("in pop of DLListHT")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e
    
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow("in pop_last DLListHT")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e
    
    

if __name__ == "__main__":
#    lst1 = LList()
#    [lst1.append(i) for i in range(20)]
#    lst1.printall()
#    print(lst1.length())

#    lst2 = LListHT()
#    [lst2.prepend(i) for i in range(20)]
#    lst2.insert(-1, 10)
#    print("lst2:")
#    lst2.printall()

    lst3 = LCList()
    [lst3.append(i) for i in range(20)]
    lst3.insert(-1, 20)
    print("lst3")
    lst3.printall()
    print("reverse:")
    lst3.rev()
    lst3.printall()

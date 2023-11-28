<<<<<<< HEAD
from random import randint

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, qtd) -> None:
        self.qtd = qtd
        self.obj = randint(1, copos)
        print(f"objeto escondido no copo {self.obj}")
        self.head = None
        self.tail = None

    def insert(self, key):
        cup = Node(key)
        cup.next = self.head
        if self.head:
            self.head.prev = self.head
        else:
            self.tail = cup
        self.head = cup

    def remove_beggining(self):
        if not self.head:
            return
        if self.head.next:
            self.head.next.prev = None
        else:
            self.tail = None
        self.head = self.head.next

    def remove_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            self.tail = None
            return
        self.tail.prev.next = None
        self.tail = self.tail.prev

    def travessia(self):
        actual = self.head
        while actual:
            print(actual.key)
            actual = actual.next
    
    def peek(self, tentativas):
        self.travessia()
        print()
        number_guess = int(input("Advinhe o copo: "))
        if number_guess == self.obj:
            print(f"Acertou!")
        else:
            if tentativas != 0:
                if number_guess == 1:
                    self.remove_beggining()
                    return self.peek(tentativas)
                elif number_guess == self.qtd:
                    self.remove_end()
                    return self.peek(tentativas)
                tentativas -= 1
            print(f"O objeto estava escondido no copo {self.obj}")



copos = int(input("Qtd de copos iniciais: "))
lista = DoubleLinkedList(copos)

for i in range(1, copos+1):
    lista.insert(f"[{i}]")


lista.peek(3)
=======
class Node:
    
>>>>>>> c39eeda246b8afee7c4ce3f572f55c4e6300bad8

from random import randint

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, qtd) -> None:
        self.qtd = qtd
        self.obj = [4]#[randint(1, copos)]
        print(f"objeto escondido no copo {self.obj}")
        self.head = None
        self.tail = None

    def insert_end(self, key):
        copo = Node(key)
        if not self.head:
            self.head = copo
            self.tail = copo
            return
        self.tail.next = copo
        copo.prev = self.tail
        self.tail = copo

    def remove_beggining(self):
        print(f"self.head1={self.head.key}")
        if not self.head:
            return
        if self.head.next:
            self.head.next.prev = None
        else:
            self.tail = None
        self.head = self.head.next
        print(f"self.head2={self.head.key}")

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
            print(actual.key, end=" ")
            actual = actual.next
    
    def peek(self, tentativas):
        print(f"\033[91mTENTATIVAS={tentativas}\033[0m")
        self.travessia()
        print()
        palpite = int(input("Advinhe o copo: "))
        palpite = [palpite]
        print(f"{palpite} == {self.obj}")
        if str(palpite) == str(self.obj):
            print(f"Acertou!")
            return
        else:
            tentativas -= 1
            if tentativas != 0:
                if str(palpite) == str(self.head.key):
                    print("Entrou AQUI")
                    self.remove_beggining()
                    return self.peek(tentativas)
                    
                '''elif palpite == self.qtd:
                    self.remove_end()
                    return self.peek(tentativas)'''
            #print(f"O objeto estava escondido no copo {self.obj}")



copos = int(input("Qtd de copos iniciais: "))
lista = DoubleLinkedList(copos)

for i in range(1, copos+1):
    lista.insert_end(f"[{i}]")


lista.peek(3)

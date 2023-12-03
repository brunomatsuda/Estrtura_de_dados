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

    def delete_front(self):
        #print(f"self.head1={self.head.key}")
        if not self.head:
            return
        if self.head.next:
            self.head.next.prev = None
        else:
            self.tail = None
        self.head = self.head.next
        #print(f"self.head2={self.head.key}")

    def delete_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            self.tail = None
            return
        self.tail.prev.next = None
        self.tail = self.tail.prev

    def delete_middle(self, node):
        current = self.head.next.key
        head = self.head
        #print(type(current))
        current = int(current[1:-1]) 
        #obj = self.obj.pop()
        #print(type(node))
        #print(f"current={current}")
        for i in range(1,node):
            print(i)
            head = head.next
        print(f"HEAD={head.key}")
        if head.prev:
            print(f"HEAD.PREV={head.prev.key}")
            head.prev.next = head.next
        if head.next:
            print(f"HEAD.NEXT={head.next.key}")
            head.next.prev = head.prev
        else:
            self.tail = head.prev


    def travessia(self):
        current = self.head
        while current:
            print(current.key, end=" ")
            current = current.next
    
    def peek(self, tentativas):
        print(f"\033[91mTENTATIVAS={tentativas}\033[0m")
        self.travessia()
        print()
        palpite = int(input("Advinhe o copo: "))
        palpite = [palpite]
        #print(type(palpite))
        #print(f"{palpite} == {self.obj}")
        if str(palpite) == str(self.obj):
            print(f"Acertou!")
            return
        else:
            tentativas -= 1
            if tentativas != 0:
                if str(palpite) == str(self.head.key):
                    self.delete_front()
                    return self.peek(tentativas)
                    
                elif str(palpite) == str(self.tail.key):
                    self.delete_end()
                    return self.peek(tentativas)
                
                else:
                    palpite = palpite.pop() #tira da lista
                    self.delete_middle(palpite)
                    return self.peek(tentativas)
            
            #print(f"O objeto estava escondido no copo {self.obj}")



copos = int(input("Qtd de copos iniciais: "))
lista = DoubleLinkedList(copos)

for i in range(1, copos+1):
    lista.insert_end(f"[{i}]")


lista.peek(3)

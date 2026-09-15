"""
권영미 교수님 코드 참조 기본 이중 연결 리스트 
"""

class DListNode:
    def __init__(self, data=None):
        self.data = data
        self.llink = None
        self.rlink = None


class DoublyLinkedList:
    def __init__(self):
        self.head = DListNode()

        self.head.llink = self.head
        self.head.rlink = self.head


    def insert(self, before, data):
        newnode = DListNode(data)

        newnode.llink = before
        newnode.rlink = before.rlink
        before.rlink.llink = newnode
        before.rlink = newnode

        return newnode


    def delete(self, removed):
        if removed == self.head:
            return

        removed.llink.rlink = removed.rlink
        removed.rlink.llink = removed.llink


    def print_list(self):
        p = self.head.rlink

        while p!= self.head:
            print(p.data, end=" ")
            p = p.rlink

        print()

if __name__ == '__main__':

    L = DoublyLinkedList()

    n1 = L.insert(L.head, 10)
    n2 = L.insert(n1, 20)
    n3 = L.insert(n2, 30)
    L.print_list()
    L.delete(n2)
    
""" 
헤드와 테일로 양방향 연결 리스트 구현
헤드는 맨 첫 노드
테일은 맨 마지막 노드
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # 첫 번째 노드와 마지막 노드를 가리킨다.
        # 리스트가 비어 있으면 둘 다 None이다.
        self.head = None
        self.tail = None

    def insert_first(self, data):
        # 리스트의 맨 앞에 새로운 노드를 삽입한다.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, data):
        # 리스트의 맨 뒤에 새로운 노드를 삽입한다.
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, target, data):
        # target 값을 가진 첫 번째 노드를 찾아
        # 그 노드의 바로 뒤에 새로운 노드를 삽입한다.
        curr = self.search(target)
        if curr is None:
            return

        if curr == self.tail:
            self.insert_last(data)
        else:
            new_node = Node(data)
            new_node.prev = curr
            new_node.next = curr.next
            curr.next.prev = new_node
            curr.next = new_node

    def delete_first(self):
        # 리스트의 첫 번째 노드를 삭제한다.
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_last(self):
        # 리스트의 마지막 노드를 삭제한다.
        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete(self, data):
        # data 값을 가진 첫 번째 노드를 찾아 삭제한다.
        # 해당 값이 없으면 아무 작업도 하지 않는다.
        curr = self.search(data)
        if curr is None:
            return

        if curr == self.head:
            self.delete_first()
        elif curr == self.tail:
            self.delete_last()
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

    def search(self, data):
        # data 값을 가진 노드를 처음부터 탐색한다.
        # 찾으면 해당 노드를 반환하고, 없으면 None을 반환한다.
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def print_forward(self):
        # head부터 tail 방향으로 모든 데이터를 출력한다.
        curr = self.head
        result = []
        while curr is not None:
            result.append(str(curr.data))
            curr = curr.next
        print(" ".join(result))

    def print_backward(self):
        # tail부터 head 방향으로 모든 데이터를 출력한다.
        curr = self.tail
        result = []
        while curr is not None:
            result.append(str(curr.data))
            curr = curr.prev
        print(" ".join(result))
"""
시간복잡도
맨 앞이나 뒤 삽입 및 삭제 O(1)
임의 위치는 O(N)
"""

# ------------------------------------
# Test
# ------------------------------------

L = DoublyLinkedList()

# 삽입 테스트
L.insert_first(20)
L.insert_first(10)
L.insert_last(30)
L.insert_last(40)

print("Forward:")
L.print_forward()
# 예상 결과: 10 20 30 40

print("Backward:")
L.print_backward()
# 예상 결과: 40 30 20 10

# 중간 삽입 테스트
L.insert_after(20, 25)

print("After insert:")
L.print_forward()
# 예상 결과: 10 20 25 30 40

# 삭제 테스트
L.delete_first()
L.delete_last()
L.delete(25)

print("After delete:")
L.print_forward()
# 예상 결과: 20 30

# 탐색 테스트
node = L.search(30)

if node is not None:
    print("Found:", node.data)
else:
    print("Not found")

# 예상 결과: Found: 30
"""
 이진 트리 (Binary Tree): 각 노드가 최대 두 개의 자식(왼쪽 자식, 오른쪽 자식)을 가지는 트리 구조
 배열 인덱스 k에 대해 부모 노드는 (k-1)/2, 왼쪽 자식은 2*k+1, 오른쪽 자식은 2*k+2의 관계
"""
# 노드를 정의
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# 이진 트리를 배열로 변환
def tree_to_array(root):
    if root is None:
        return []

    array = []
    queue = [(root, 0)]

    while queue:
        node, index = queue.pop(0)

        if index >= len(array):
            array.extend([None] * (index - len(array) + 1))#부족한 길이를 확장
        
        array[index] = node.key#노드의 키를 배열에 저장
        
        #다음 순환을 위한 큐에 자식노드값 추가
        if node.left:
            queue.append((node.left, 2 * index + 1))
        if node.right:
            queue.append((node.right, 2 * index + 2))

    return array
#이진  트리 생성
binary_tree_root = Node(2)
binary_tree_root.left = Node(7)
binary_tree_root.right = Node(52)
binary_tree_root.left.left = Node(13)
binary_tree_root.left.right = Node(8)
binary_tree_root.right.left = Node(67)
binary_tree_root.right.right = Node(161)
binary_tree_root.left.left.left = Node(17)
binary_tree_root.left.left.right = Node(43)
binary_tree_root.left.right.left = Node(88)
binary_tree_root.left.right.right = Node(37)

# 결과 출력
array_representation = tree_to_array(binary_tree_root)
print(array_representation)
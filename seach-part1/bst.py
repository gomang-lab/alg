# 노드 클래스
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# 값 찾기 (재귀)
def treeSearch(t, x):
    # 비어있거나 찾던 값이면 리턴
    if t is None or t.key == x:
        return t
    
    # 찾는 값이 작으면 왼쪽으로
    if x < t.key:
        return treeSearch(t.left, x)
    # 크면 오른쪽으로
    else:
        return treeSearch(t.right, x)
"""
# 노드 삽입하기
def treeInsert(t, x):
    # 빈 자리를 만나면 새 노드 만들기
    if t is None:
        return Node(x)
    
    # 작으면 왼쪽 자리에 넣기
    if x < t.key:
        t.left = treeInsert(t.left, x)
    # 크면 오른쪽 자리에 넣기
    else:
        t.right = treeInsert(t.right, x)
    return t
"""
# 반복문 노드 삽입
def treeInsert(t, x):
    # 새 노드 r 생성 및 초기화 (r.key <- x, r.left <- NIL, r.right <- NIL)
    r = Node(x)
    
    # 만약 트리가 비어있다면, 새 노드가 루트가 됨
    if t is None:
        return r
    p = None       # 부모 노드를 기억할 변수
    tmp = t        # 트리를 탐색할 임시 변수
    # 잎 노드(None)에 도달할 때까지 아래로 내려감
    while tmp is not None:
        p = tmp    # 현재 노드를 부모로 기억
        if x < tmp.key:
            tmp = tmp.left  # 작으면 왼쪽으로
        else:
            tmp = tmp.right # 크면 오른쪽으로
    # 반복문이 끝난 후, 부모(p)와 비교하여 적절한 위치에 새 노드 매달기
    if x < p.key:
        p.left = r   
    else:
        p.right = r  
    return t         # 루트 노드 반환
# 노드 삭제하기
def deleteNode(root, key):
    # 트리가 비어있거나 찾는 값이 없는 경우
    if root is None:
        return root

    # 삭제할 값이 현재 노드보다 작으면 왼쪽에서 찾아서 지움
    if key < root.key:
        root.left = deleteNode(root.left, key)
    # 삭제할 값이 현재 노드보다 크면 오른쪽에서 찾아서 지움
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    # 삭제할 노드를 찾은 경우
    else:
        # 자식이 없는 경우
        if root.left is None and root.right is None:
            return None
        
        # 왼쪽 자식만 없는 경우
        elif root.left is None:
            return root.right
        
        # 오른쪽 자식만 없는 경우 
        elif root.right is None:
            return root.left
        
        # 자식이 둘 다 
        else:
            # 오른쪽 서브트리에서 가장 작은 값(후속자) 찾기
            s = root.right
            while s.left is not None:
                s = s.left
            
            # 후속자의 값을 현재 노드에 덮어쓰기
            root.key = s.key
            
            # 중복된 값을 가진 후속자 노드를 오른쪽 서브트리에서 삭제하기
            root.right = deleteNode(root.right, s.key)
    return root
# 트리 출력 중위순회 오름차순
def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.key, end=" ")
        inorder(t.right)

# 메인 실행
if __name__ == "__main__":
    root = None
    
    # 데이터 넣기
    data = [50, 30, 70, 20, 40, 60, 80]
    for val in data:
        root = treeInsert(root, val)
    #넣은 값 출력 확인
    inorder(root)
    # 값 검색
    result = treeSearch(root, 40)
    if result:
        print("성공")
    else:
        print("실패")
    # 3. 삭제
    deleteNode(root, 80)
    inorder(root)
    
    
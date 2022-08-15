class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 보통 헤더를 선언하여 연결리스트를 생성하고, 헤더를 통해 다른 모든 노드를 탐색하고
# 참조할 수 있다. 따라서, head를 직접 이동시키지 않고, node = head로 head 주소를 참조하여
# 사용한다.(헤더는 data를 포함하고 있지 않으며, 헤더의 다음 노드로부터 데이터를 가지나 편의상 임의의
# 값을 넣고 다음 노드부터 사용해도 되고, head노드부터 사용해도 된다.)

def insertionSortList(self, head:ListNode) -> ListNode:
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        #필요한 경우에만 cur 포인터가 되돌아가도록 처리
        if head and cur.val > head.val:
            cur = parent

        return parent.next

#큐 연산
# enQueue(item): 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산
# deQueue(): 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산
# createQueue(): 공백상태의 큐를 생성하는 연산
# isEmpty(): 큐가 공백상태인지를 확인하는 연산
# isFull(): 큐가 포화상태인지를 확인하는 연산
# Qpeek(): 큐의 앞쪽에서 원소를 삭제 없이 반환하는 연산
#     현재 front의 한자리 뒤(front+1)에있는 원소, 즉 큐의 첫번째에 있는 원소를 반환
# front와 rear가 같으면 queue가 비어 있는 상태라고 판단.
# front: 저장된 첫번째 원소의 인덱스
# rear: 저장된 마지막 원소의 인덱스
# 상태표현
#     초기상태: front = rear = -1
#     공백상태: front ==rear
#     포화상태: rear == n-1(n: 배열의 크기, n-1 배열의 마지막 인덱스)
#
# 선형큐 이용시의 문제점
#     잘못된 포화상태 인식:
#         선형큐를 이용하여 삽입과 삭제를 계속할 경우 배열의 앞부분을
#         활용할 수 있는 공간이 있음에도 불구하고, rear = n-1인 상태, 즉 포화상태로 인삭하여
#         더이상의 삽입 수행하지 않음.
#     해결방법: 원형큐
#         1차원 배열을 사용하되 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고
#         가정하고 사용.
#
# 원형큐의 구조
#     과거의 데이터가 필요없을때
#     초기 공백상태: front = rear = 0
#     index의 순환
#         front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을
#         이루어 배열의 처음 인덱스인 0으로 이동해야 함.
#         이를 위해 나머지 연산자 mod(%) 를 사용함
# 원형큐의 구현
# def enQueue(item):
#     golbla rear
#     if isFull():
#         print("Queue_full")
#     else:
#         rear = (rear + 1) % len(cQ)
#         cQ[rear] = item
# def deQueue():#front값을 조정하여 삭제할 자리를 준비함. 새로운 원소를 return 함으로 삭제와 동일한 기능.
#     golbla front
#     if isEmpty():
#         print("Queue_Empth")
#     else:
#         front = (front + 1) % len(cQ)
#         return cQ[front]
# def isEmpty():
#     return fornt == rear
# def isFull():
#     return (rear+1) % len(cQ) == front


n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
n_lst.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 더 작은 경우 왼쪽 확인
    if array[mid] > target:
        return binary_search(array,target,start,mid-1)
    #중간점의 값보다 찾고자 하는 값이 더 큰 경우 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)

# binary_search 사용
for i in m_lst:
    result = binary_search(n_lst,i,0,n-1)
    if result == None:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')
print()

# # 내장함수 in 사용
for j in m_lst:
    if j in n_lst:
        print('yes', end =' ')
    else:
        print('no', end=' ')

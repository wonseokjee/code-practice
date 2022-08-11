from collections import deque
#이 문제는 대소문자를 구분하지 않으며 영문자, 숫자만을 대상으로 한다는 제약조건.
#전처리
s = input()
# strs= []
strs: str = deque()
for char in s:
    if char.isalnum():                      #isalnum은 영문자, 숫자 여부를 판별하는 함수.
        strs.append(char.lower())           #대소문자 구분 x 모두 소문자로 변환=0
while len(strs) > 1:
    # if strs.pop(0) != strs.pop():           #리스트의 맨앞, 맨뒤를 삭제하면서 비교
    if strs.popleft() != strs.pop():
        print(False)                        #맨 앞 맨뒤 같지 않으면
        break
print(True)
# if strs == 0 or len(strs) == 1:             #pop으로 모두 꺼내지거나 가운데 하나 남으면 True 출력
#     print(True)
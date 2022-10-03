# 1. 쿼리의 ? 개수를 어떻게 세고 어디에 있는지를 어떻게 정의?
# 2. 쿼리의 result 생성
# 3. word하나하나를 쿼리와 비교. 맞으면
# 4. queries를 문자,길이,문자의 슬라이싱주소로 리스트화?
from heapq import heapify

word = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
len_qu = len(queries)
result = [0]*len_qu # result값.
heapify(word)
print(word)

for i in range(len_qu):
    for j in word:
        if len(queries[i]) == len(j): # 길이확인
            cnt = 0
            num = 0
            for k in range(len(queries[i])):
                if queries[i][k].isalpha():
                    cnt += 1
                    if queries[i][k] == j[k]:
                        num += 1
            if cnt == num:
                result[i]+= 1
print(result)



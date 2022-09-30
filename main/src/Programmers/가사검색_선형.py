# 1. 쿼리의 ? 개수를 어떻게 세고 어디에 있는지를 어떻게 정의?
# 2. 쿼리의 result 생성
# 3. word하나하나를 쿼리와 비교. 맞으면
# 4. queries를 문자,길이,문자의 슬라이싱주소로 리스트화?



word = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = [0]*len(queries) # result값.
query = []

for i in queries:
    cnt = len(i)
    num = len(i)
    wd = ''
    for j in range(len(i)):
        if cnt ==len(i) and i[j].isalpha():
            cnt = j
        if num == len(i) and not i[j].isalpha():
            num = j
        if i[j].isalpha():
          wd += i[j]
    query.append([wd,len(i),cnt,num])
# print(query)

aaa = 0
for k in word:
    for l in query:
        if len(k) == l[1]:
            if l[3] ==0:
                if l[0] == k[l[2]:l[1]]:
                    result[aaa] += 1
            else:
                if l[0] == k[l[2]:l[3]]:
                    result[aaa] += 1
        aaa+= 1
    aaa = 0
print(result)


# 리스트의 왼쪽부터 설치하다가 막히면 오른쪽에서 설치
# 막히면 다시 왼쪽으로 왼쪽도 막히면 무시
# 무시하고 다시 막히면 오른쪽으로, 이번에도 막히면 무시.
# 막힐때마다 왼쪽방향 카운트 오른쪽 방향 카운트
# 2되면 무시하고고초기화

# 보는 양쪽이 보인지 확인 / 오른쪽아래, 바로 아래 기둥인지 확인.
# 기둥은 아래가 바닥or기둥, 왼쪽이나 같은좌표가 보

# 삭제시에는 기둥이빠지면 위의 기둥과 위의양옆보가 설치가능한지
# 보가빠지면 양옆 보와 같은좌표,오른쪽 기둥이 설치가능한지


n = int(input())
build_frame = input()
frame_len = len(build_frame)
result =  []
def create(x,y,a,b):
    if a == 0:#기둥일때
        if y==0 or [x,y-1,0] in result:
            return
        elif [x-1,y,1] or [x,y,1] in result:
            return
    elif a == 1: #보일때
        if [x-1,y,1] in result and [x+1,y,1] in result:  #양쪽인 보인지
            return
        elif [x+1,y-1,0] in result or [x,y-1,0] in result: # 오른쪽아래, 바로 아래가 기둥인지
            return
    else:
        return '설치 불가능'

cnt= 0
for i in range(frame_len):
    if len(build_frame) >0:
        x,y,a,b = build_frame[i]
        if create(x,y,a,b) =='설치가능':
            result.append([x,y,a])
        elif create(x,y,a,b) =='설치 불가능':
            pass
print(build_frame)




# 5
# [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
#[[1,0,0,1], x,y,a,b
# [1,1,1,1], x,y = 좌표
# [2,1,0,1], a = 0은 기둥 1은 보
# [2,2,1,1], b = 0삭제 1 설치
# [5,0,0,1],
# [5,1,0,1],
# [4,2,1,1],
# [3,2,1,1]]

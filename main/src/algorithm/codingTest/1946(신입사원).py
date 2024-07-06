import sys
input = sys.stdin.readline
T = int(input())
for _ in range(1,T+1):
    tc = int(input())
    lst = []
    set_cnt = set([])
    for _ in range(tc):
        paper,interview = map(int,input().split())
        lst.append([paper,interview])
    paper_sort = sorted(lst)
    interview_sort = sorted(lst, key=lambda x:x[1])
    # print(paper_sort)
    # print(interview_sort)
    for i in range(1,tc):
        # print(i)
        if paper_sort[i-1][1] < paper_sort[i][1]:
            # print(f'paper = {paper_sort[i]}')
            set_cnt.add((paper_sort[i][0],paper_sort[i][1]))
        if interview_sort[i-1][0]<interview_sort[i][0]:
            # print(f'interveiw = {interview_sort[i]}')
            set_cnt.add((interview_sort[i][0],interview_sort[i][1]))
    print(tc - len(set_cnt))
# 1
# 6
# 6 4
# 4 1
# 5 2
# 1 6
# 2 3
# 3 5

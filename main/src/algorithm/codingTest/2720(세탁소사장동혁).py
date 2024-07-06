T = int(input())
for tc in range(T):
    C = int(input())
    q = 0
    d = 0
    n = 0
    p = 0
    q_l = C % 25
    q_a = C // 25
    d_l = q_l % 10
    d_a = q_l // 10
    n_l = d_l % 5
    n_a = d_l // 5
    print(q_a,d_a,n_a,n_l)
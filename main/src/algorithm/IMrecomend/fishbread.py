T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int, input().split())
    arr = list(map(int,input().split()))
    last = max(arr)
    bread = 0
    cnt = 0
    for i in range(1,last+1):
        if i%M==0:
            bread += K

        while (True):
            if i in arr:
                x = arr.index(i)
                arr[x] = 0
                if bread > 0:
                    bread -= 1
                    cnt += 1
            else:
                break
    print(f'#{tc}', end=' ')
    if cnt == len(arr):
        print('Possible')
    else:
        print('Impossible')

# 92 99 71
# 2021 673 8235 10089 7547 1849 9837 10538 1115 10966 8938 8770 5706 1868 325 8002 5470 8943 6525 9142 9845 4458 2863 4427 2425 4889 2623 10932 686 8472 1378 10297 2716 3875 9522 930 1132 7590 1212 2705 9386 6949 7076 3559 7353 8535 10297 9279 2162 3803 3262 4611 3271 3464 6923 9332 4961 2241 8570 4801 3203 3971 10508 9764 938 9075 289 4359 4384 1639 10038 7371 571 1248 501 1925 9628 9856 1131 2976 2211 4344 8383 3054 7539 8423 6823 1371 9528 6097 11086 9268
# 77 47 75
# 7268 6245 2757 3477 4022 5916 3048 1827 3190 6277 4506 466 7187 7384 8048 9322 8582 4802 814 8509 4882 6603 9810 263 3261 10345 1827 4821 4923 9772 8169 8621 4023 3683 2660 1478 8588 9234 262 9307 1195 1848 4577 5489 7390 2188 3488 6643 419 935 6762 8999 6273 9618 918 1922 3339 1733 5834 8713 4850 381 3493 6268 6008 3092 4090 7138 6212 2128 7727 8146 797 8478 9773 2987 2393
# 97 6 84
# 9187 5243 10920 5158 1284 2901 8012 9382 977 5990 5951 600 6910 9070 10244 5746 9037 10438 3892 9806 2429 5571 8286 2203 10378 1379 2738 6834 1838 5574 3161 10653 7449 8608 10607 943 8082 8598 5732 8859 6419 10347 625 5666 9338 3694 4294 11068 4963 9710 9208 6362 3445 10512 321 4165 2920 1447 1211 11006 603 2673 4197 6662 30 10438 8562 1333 2578 4454 5990 6054 133 8528 9963 9886 2915 9325 9113 7869 2734 555 3193 5806 8965 955 929 8407 10928 4217 4382 8872 2256 5130 3833 2327 1422

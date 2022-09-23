import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
   num_2 = list(map(str, input()))
   num_3 = list(map(str, input()))
   ins_2 = []
   ins_3 = []
   def guess(num_2):
       if num_2[i] == '0':
           num_2[i] = '1'
       else:
           num_2[i] = '0'

   def guess_3(num_3):
       if num_3[a] == '0':
           num_3[a] = '1'
       elif num_3[a] == '1':
           num_3[a] = '2'
       else:
           num_3[a] = '0'

   for i in range(len(num_2)):
       guess(num_2)
       cnt = 0
       for j in range(len(num_2)):
           cnt = cnt * 2 + int(num_2[j])
       ins_2.append(cnt)
       guess(num_2)

   for a in range(len(num_3)):
       guess_3(num_3)
       cnt_1 = 0
       for b in range(len(num_3)):
           cnt_1 = cnt_1 * 3 + int(num_3[b])
       ins_3.append(cnt_1)

       guess_3(num_3)
       cnt_2 = 0
       for k in range(len(num_3)):
           cnt_2 = cnt_2 * 3 + int(num_3[k])
       ins_3.append(cnt_2)
       guess_3(num_3)
   for g in range(len(ins_2)):
       if ins_2[g] in ins_3:
           print(f'#{tc} {ins_2[g]}')

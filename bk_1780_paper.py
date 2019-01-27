Number = int(input())
S = list()
for idx in range(Number):
    Sstring = input()
    S[idx] = Sstring

print(S)

import numpy as np
count1 = 0
count0 = 0
countn = 0

def DQ(target_list, num):
    same_check = False
    if num == 1:
       same_check = False
    else:
        tmp_value = target_list[0][0]
        for i in target_list:
            for j in i:
                #condition
                if tmp_value != j:
                    same_check = True
    #when condition met
    if same_check == False:
        if target_list[0][0] == 1:
            global count1 
            count1 += 1
        elif target_list[0][0] == 0:
            global count0
            count0 += 1
        else:
            global countn
            countn += 1
    else:
        target_list = np.array(target_list)
        tmp1 = target_list[:int(num/3), :int(num/3)]; DQ(tmp1.tolist(), num/3)
        print(tmp1.tolist())
        tmp2 = target_list[:int(num/3), int(num/3):int(num/3*2)]; DQ(tmp2.tolist(), num/3)
        print(tmp2.tolist())
        tmp3 = target_list[:int(num/3), int(num/3*2):]; DQ(tmp3.tolist(), num/3)
        tmp4 = target_list[int(num/3):int(num/3*2), :int(num/3)]; DQ(tmp4.tolist(), num/3)
        tmp5 = target_list[int(num/3):int(num/3*2), int(num/3):int(num/3*2)]; DQ(tmp5.tolist(), num/3)
        tmp6 = target_list[int(num/3):int(num/3*2), int(num/3*2):]; DQ(tmp6.tolist(), num/3)
        tmp7 = target_list[int(num/3*2):, :int(num/3)]; DQ(tmp7.tolist(), num/3)
        tmp8 = target_list[int(num/3*2):, int(num/3):int(num/3*2)]; DQ(tmp8.tolist(), num/3)
        tmp9 = target_list[int(num/3*2):, int(num/3*2):]; DQ(tmp9.tolist(), num/3)



num = 9
target_list1 = [[0, 0, 0, 1, 1, 1, -1, -1, -1],
[0, 0, 0, 1, 1, 1, -1, -1, -1],
[0, 0, 0, 1, 1, 1, -1, -1, -1],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 1, -1, 0, 1, -1, 0, 1, -1],
[0, -1, 1, 0, 1, -1, 0, 1, -1],
[0, 1, -1, 1, 0, -1, 0, 1, -1]]

DQ(target_list1, num)
print(count1)
print(count0)
print(countn)
num = int(input())
arr1 = input().split(',')
arr1 = [int(i) for i in arr1]
arr2 = input().split(',')
arr2 = [int(i) for i in arr2]
#for test
#print(num)
#print(arr1)
secret_map = [[0 for cols in range(num)]for rows in range(num)]
solution_map = list()
def Solution(arr, secret_map):
    idx = 0
    while idx < num:
        #tmp_value = arr_tmp[idx]

        tmp_value = arr[idx]

        tmp_num = num
        idx_cols = 0
    
        while idx_cols < num:
            if tmp_value - (2**(tmp_num-1)) >= 0:
                tmp_value = tmp_value - (2**(tmp_num-1))
                secret_map[idx][idx_cols] += 1
       
            tmp_num = tmp_num-1    
            idx_cols = idx_cols+1
        idx = idx+1

    return secret_map

secret_map = Solution(arr1, secret_map)
secret_map = Solution(arr2, secret_map)

for i in secret_map:
    tmp = ""
    for j in i:
        if j > 0:
            tmp += "#"
        else:
            tmp += " "
    solution_map.append(tmp)


print(solution_map)
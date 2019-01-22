def solution_1(n, arr1, arr2):
    bin_arr1 = list(map(lambda x: bin(x)[2:].zfill(n), arr1))
    bin_arr2 = list(map(lambda x: bin(x)[2:].zfill(n), arr2))
    decoded = []
    for row in range(0, n):
        decoded.append("")
        for column in range(0, n):
            if not (int(bin_arr1[row][column]) or int(bin_arr2[row][column])):
                decoded[row] += " "
            else:
                decoded[row] += "#"
    return decoded

def solution_2(n, arr1, arr2):
    decoded = []
    for i in range(n):
        decoded.append(format(arr1[i] | arr2[i], 'b').zfill(n))
    decoded = list(map(lambda x: x.replace("1", "#").replace("0", " "), decoded))
    return decoded
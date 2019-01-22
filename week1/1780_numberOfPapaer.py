def CheckAllSame(paper):
    checking_number = paper[0][0]
    for row in paper:
        for element in row:
            if element != checking_number:
                return False
    return True
    # return len(set.union(set(paper[i])) for i in range(len(paper))) == 1

def CheckPaper(paper, result):
    if CheckAllSame(paper):
        result[paper[0][0]] += 1
    else:
        scale = len(paper) // 3
        for i in range(3):
            for j in range(3):
                sliced_paper = [paper[i][j * scale : (j + 1) * scale] for i in range(i * scale, (i + 1) * scale)]
                CheckPaper(sliced_paper, result)

N = int(input())
paper = []
result = {"-1" : 0, "0" : 0, "1" : 0}

for row in range(N):
    new_row = list(input().split())
    paper.append(new_row)

CheckPaper(paper, result)
print(result["-1"])
print(result["0"])
print(result["1"])

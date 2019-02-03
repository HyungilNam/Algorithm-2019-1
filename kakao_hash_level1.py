#kakao practice>hash>infinished runner

#participant : ["leo", "kiki", "eden"]
#completion : ["eden","kiki"]

def InfinishedRunner(participant, completion):
    answer = ''
    result = {}

    for k in participant:
        result[k] = 0

    for k in participant:
	result[k] += 1

    for j in completion:
        result[j] -= 1

    for i in participant:
        if result[i] > 0:
            answer = i
            break
    print(answer)
    #return answer


participant = ["leo", "kiki", "eden"]
completion = ["eden","kiki"]
InfinishedRunner(participant, completion)

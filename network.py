def solution(n, computers):
    answer = 0
    anslist = []
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j] == 1:
                anslist.append([i,j])

    for s in anslist:
        #print(s)
        if [s[1],s[0]] in anslist:
            anslist.pop(0)
            answer+=1
        
    return n - answer

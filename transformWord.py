def DFS(begin,target,words,visited,depth):
    queue = []
    if begin==target:
        return depth
    for idx,word in enumerate(words):
        hit = 0
        if visited[idx]==0 and begin!=word:
            for i in range(len(begin)):
                if begin[i] != word[i]:
                    hit+=1
            if hit == 1:
                queue.append(word)
    while queue:
        top = queue.pop()
        visited[words.index(top)] = 1
        return DFS(top,target,words,visited,depth+1)
        

def solution(begin, target, words):
    answer = []
    visited = [0 for i in range(len(words))]
    if target not in words:
        return 0
    answer = DFS(begin,target,words,visited,0)
    return answer

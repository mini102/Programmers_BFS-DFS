def BFS(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    return leaves.count(target)

def DFS(numbers,target,depth):
    ans = 0
    if depth+1 == len(numbers):
        if sum(numbers)==target:
            return 1
        else: return 0
    ans+= DFS(numbers,target,depth+1)
    numbers[depth]*=-1
    ans+= DFS(numbers,target,depth+1)
    print("ans")
    return ans

def anotherDFS(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer

def solution(numbers,target):
    answer = 0
    #answer = BFS(numbers,target)
    #answer = anotherDFS(numbers,target)
    answer = DFS(numbers,target,0)
    return answer

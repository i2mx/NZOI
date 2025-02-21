import math
from heapq import heappop, heappush   
from pprint import pprint

N, M, K = map(int, input().split())
# 0 <= K,N,M <= 100
S = input()
E = input()

word_list = [input() for _ in range(M)]
start = word_list.index(S)
end = word_list.index(E)

# string to list of strings
# + cost

graph = [[(101, 101) for _ in range(M)] for _ in range(M)]


def shortest_path_with_cost_limit(graph, start, end, K):
    # Initialize distances and priority queue
    dist = [[math.inf for cost in range(K+1)] for node in graph]
    dist[start][0] = 0
    pq = [(0, 0, start)]  # (current_distance, current_cost, current_node)
    
    while pq:
        current_distance, current_cost, u = heappop(pq)
        
        if u == end and current_cost <= K:
            return current_distance
        
        if current_distance > dist[u][current_cost]:
            continue
        
        for v in range(M):
            if u == v:
                continue
            weight, cost = graph[u][v]

            new_distance = current_distance + weight
            new_cost = current_cost + cost
            
            if new_cost <= K and new_distance < dist[v][new_cost]:
                dist[v][new_cost] = new_distance
                heappush(pq, (new_distance, new_cost, v))
    
    return "IMPOSSIBLE"  # if no valid path is found

for i, word1 in enumerate(word_list):
    for j, word2 in enumerate(word_list):
        if i == j:
            continue
        diff = 0
        for k in range(N):
            if word1[k] != word2[k]:
                diff += 1
        graph[i][j] = (diff, diff - 1)


a = shortest_path_with_cost_limit(graph, start, end, K) 
print(a)

# connect words in the word list if they differ by one letter
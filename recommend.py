# recommend.py
from collections import Counter, deque
import heapq

def mutual_friend_recommendations(graph, user_id, top_k=5):
    friends = graph.get_friends(user_id)
    mutual_counts = Counter()

    for friend in friends:
        for fof in graph.get_friends(friend):
            if fof != user_id and fof not in friends:
                mutual_counts[fof] += 1

    return heapq.nlargest(top_k, mutual_counts.items(), key=lambda x: x[1])

def bfs_shortest_path_recommendation(graph, user_id, top_k=5):
    visited = set()
    queue = deque([(user_id, 0)])
    shortest_paths = {}

    while queue:
        current, depth = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        if current != user_id and current not in graph.get_friends(user_id):
            if current not in shortest_paths or depth < shortest_paths[current]:
                shortest_paths[current] = depth

        for neighbor in graph.get_friends(current):
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))

    return heapq.nsmallest(top_k, shortest_paths.items(), key=lambda x: x[1])

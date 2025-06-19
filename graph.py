# graph.py
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(set)

    def add_user(self, user_id):
        if user_id not in self.adj_list:
            self.adj_list[user_id] = set()

    def add_friendship(self, user1, user2):
        self.adj_list[user1].add(user2)
        self.adj_list[user2].add(user1)

    def delete_user(self, user_id):
        for friend in self.adj_list[user_id]:
            self.adj_list[friend].remove(user_id)
        del self.adj_list[user_id]

    def delete_friendship(self, user1, user2):
        self.adj_list[user1].discard(user2)
        self.adj_list[user2].discard(user1)

    def get_users(self):
        return list(self.adj_list.keys())

    def get_friends(self, user_id):
        return self.adj_list.get(user_id, set())

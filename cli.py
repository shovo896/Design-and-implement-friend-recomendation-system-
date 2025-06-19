# cli.py
from graph import Graph
from recommend import mutual_friend_recommendations, bfs_shortest_path_recommendation
from utils import export_csv

def cli(graph):
    while True:
        print("\n--- Friend Recommendation CLI ---")
        print("1. Add User")
        print("2. Add Friendship")
        print("3. Delete User")
        print("4. Recommend Friends (Mutual)")
        print("5. Recommend Friends (BFS)")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Select option: ")

        if choice == '1':
            uid = input("Enter user ID: ")
            graph.add_user(uid)

        elif choice == '2':
            u1 = input("User 1: ")
            u2 = input("User 2: ")
            graph.add_friendship(u1, u2)

        elif choice == '3':
            uid = input("Enter user ID to delete: ")
            graph.delete_user(uid)

        elif choice == '4':
            uid = input("User ID: ")
            recs = mutual_friend_recommendations(graph, uid)
            print("Recommendations:", recs)

        elif choice == '5':
            uid = input("User ID: ")
            recs = bfs_shortest_path_recommendation(graph, uid)
            print("Shortest-path Recommendations:", recs)

        elif choice == '6':
            uid = input("User ID: ")
            recs = mutual_friend_recommendations(graph, uid)
            export_csv(uid, recs)

        elif choice == '7':
            break
        else:
            print("Invalid option!")

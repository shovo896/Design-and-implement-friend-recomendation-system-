# gui.py
import tkinter as tk
from tkinter import messagebox, scrolledtext
from graph import Graph
from recommend import mutual_friend_recommendations, bfs_shortest_path_recommendation
from utils import export_csv

graph = Graph()

def add_user():
    uid = entry_user.get()
    if uid:
        graph.add_user(uid)
        messagebox.showinfo("Success", f"User '{uid}' added.")
    else:
        messagebox.showerror("Error", "Enter a user ID.")

def add_friendship():
    u1 = entry_f1.get()
    u2 = entry_f2.get()
    if u1 and u2:
        graph.add_friendship(u1, u2)
        messagebox.showinfo("Success", f"Friendship added between {u1} and {u2}.")
    else:
        messagebox.showerror("Error", "Enter both user IDs.")

def delete_user():
    uid = entry_user.get()
    if uid:
        graph.delete_user(uid)
        messagebox.showinfo("Success", f"User '{uid}' deleted.")
    else:
        messagebox.showerror("Error", "Enter a user ID to delete.")

def recommend(method):
    uid = entry_rec.get()
    if not uid:
        messagebox.showerror("Error", "Enter a user ID.")
        return
    if method == "mutual":
        results = mutual_friend_recommendations(graph, uid)
    else:
        results = bfs_shortest_path_recommendation(graph, uid)

    output_box.delete("1.0", tk.END)
    if results:
        for r in results:
            output_box.insert(tk.END, f"{r[0]}: {r[1]}\n")
    else:
        output_box.insert(tk.END, "No recommendations found.")

def export():
    uid = entry_export.get()
    if not uid:
        messagebox.showerror("Error", "Enter a user ID.")
        return
    results = mutual_friend_recommendations(graph, uid)
    export_csv(uid, results)
    messagebox.showinfo("Exported", f"CSV saved for {uid}.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Friend Recommendation System")

# Add User
tk.Label(root, text="Add User").grid(row=0, column=0)
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1)
tk.Button(root, text="Add", command=add_user).grid(row=0, column=2)
tk.Button(root, text="Delete", command=delete_user).grid(row=0, column=3)

# Add Friendship
tk.Label(root, text="Add Friendship").grid(row=1, column=0)
entry_f1 = tk.Entry(root)
entry_f2 = tk.Entry(root)
entry_f1.grid(row=1, column=1)
entry_f2.grid(row=1, column=2)
tk.Button(root, text="Add", command=add_friendship).grid(row=1, column=3)

# Recommend
tk.Label(root, text="Recommend for").grid(row=2, column=0)
entry_rec = tk.Entry(root)
entry_rec.grid(row=2, column=1)
tk.Button(root, text="Mutual", command=lambda: recommend("mutual")).grid(row=2, column=2)
tk.Button(root, text="BFS", command=lambda: recommend("bfs")).grid(row=2, column=3)

# Output Box
tk.Label(root, text="Recommendations").grid(row=3, column=0, pady=10)
output_box = scrolledtext.ScrolledText(root, width=50, height=10)
output_box.grid(row=4, column=0, columnspan=4, padx=10)

# Export
tk.Label(root, text="Export CSV for").grid(row=5, column=0)
entry_export = tk.Entry(root)
entry_export.grid(row=5, column=1)
tk.Button(root, text="Export", command=export).grid(row=5, column=2)

root.mainloop()

# utils.py
import csv

def export_csv(user_id, recommendations):
    filename = f"{user_id}_recommendations.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User", "Score/Distance"])
        writer.writerows(recommendations)
    print(f"Exported to {filename}")

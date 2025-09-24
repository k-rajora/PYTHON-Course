import csv

# Writing CSV
rows = [
    ["name", "role", "team"],
    ["Alice", "DevOps", "Platform"],
    ["Bob", "Developer", "Backend"]
]
with open("team.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Reading CSV
with open("team.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import csv

# Read the CSV file
with open("stock.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

# Reduce stock for a given item (example: Medal)
for row in data:
    if row[0] == "Medal" and int(row[1]) > 0:  # Reduce Medal stock
        row[1] = str(int(row[1]) - 1)

# Write updated stock back to CSV
with open("stock.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

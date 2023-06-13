import csv
import random

# Define the number of GPNGroups to add to Organizational Units
totalgroups = 1000

# Read the CSV file into a list of dictionaries
with open('ou_structure.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    data = [row for row in reader]

# Create a new list of dictionaries with added GPNGroups
newdata = []
for i, row in enumerate(data):
    # Generate a random number of groups to add to this OU
    numgroups = random.randint(10, totalgroups)
    # Generate group names with GPNGroup and a number
    groupnames = [f"GPNGroup{i + 1}-{j}" for j in range(1, numgroups + 1)]
    # Add the group names to the dictionary and append to the new list
    for groupname in groupnames:
        newrow = {'Group': groupname}
        newrow.update(row)
        newdata.append(newrow)

# Write the new list of dictionaries to a CSV file with Group as the first column
with open('ou_structure_with_groups.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=newdata[0].keys(), delimiter=';')
    writer.writeheader()
    writer.writerows(newdata)

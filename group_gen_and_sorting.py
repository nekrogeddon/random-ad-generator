import csv
import random
import string

# Define the number of GPNGroups to add to Organizational Units
totalgroups = 100

# Read the CSV file into a list of dictionaries
with open('ou_structure.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    data = [row for row in reader]

# Create a new list of dictionaries with added GPNGroups
newdata = []
for row in data:
    # Generate a random number of groups to add to this OU
    numgroups = random.randint(10, totalgroups)
    # Generate random group names
    groupnames = ['GPNGroup' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for i in range(numgroups)]
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
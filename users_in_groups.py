import csv
import random

# Чтение данных из CSV файлов
with open('ou_structure_with_groups.csv', mode='r', encoding='utf-8', newline='') as ou_file:
    reader = csv.reader(ou_file, delimiter=';')
    headers = next(reader, None)
    groups_list = [row[0] for row in reader]

with open('users.txt', mode='r', encoding='utf-8', newline='') as users_file:
    users_list = [row.strip() for row in users_file]

# Словарь групп из файла ou_structure_with_groups.csv и их OUPath
groups_dict = {group: {'users': [], 'path': ''} for group in groups_list}

# Заполнение OUPath в словаре groups_dict
with open('ou_structure_with_groups.csv', mode='r', encoding='utf-8', newline='') as ou_file:
    reader = csv.reader(ou_file, delimiter=';')
    headers = next(reader, None)
    for row in reader:
        ou_path = row[1:]
        for i, ou_name in enumerate(ou_path):
            if ou_name:
                if i > 0 and not groups_dict[row[0]]['path'].endswith(','):
                    groups_dict[row[0]]['path'] += ','
                groups_dict[row[0]]['path'] += ou_name

# Случайное заполнение списка пользователей в каждой группе в словаре groups_dict,
# пока в каждой группе не будет как минимум 10 пользователей.
while not all(len(info['users']) >= 10 for info in groups_dict.values()):
    random_user = random.choice(users_list)
    random_group = random.choice(list(groups_dict.keys()))
    groups_dict[random_group]['users'].append(random_user)

# Запись результата в users_in_groups_in_ou.csv
with open('users_in_groups_in_ou.csv', mode='w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    writer.writerow(['Username', 'Group', 'OUPath'])
    for group, info in groups_dict.items():
        for user in info['users']:
            writer.writerow([user, group, info['path']])
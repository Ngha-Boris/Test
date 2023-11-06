import random

members = ["Bismark", "Jude", "Sinke", "Noel", "Rodrick", "Emmanuella", "Scott", "Bryan", "Victor", "Kufang", "Forkim", "Caleb", "Nancy", "Schekina", "Victoire", "Blessing", "Bertrand", "Leku", "Ariel", "Valentine", "Hans", "Christian", "Boris"]

# Shuffle the member list
random.shuffle(members)

# Divide members into groups
groups = []
girls = ["Nancy", "Schekina", "Blessing", "Emmanuella"]

for girl in girls:
    group = [girl]
    groups.append(group)
    members.remove(girl)

group_size = 6
remaining_members = len(members)

for i in range(len(groups)):
    group = groups[i]
    while len(group) < group_size and remaining_members > 0:
        member = random.choice(members)
        group.append(member)
        members.remove(member)
        remaining_members -= 1

# Print the groups
print("Groups for the project:")

for i, group in enumerate(groups):
    print(f"Group {i+1}: {group}")
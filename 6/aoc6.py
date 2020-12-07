
with open("input", 'r') as f:
    data = f.read()


data = data.split("\n\n")

groups = []
for x, d in enumerate(data):
    individual_users = [set()]
    user = 0
    for c in d:
        if c == "\n":
            user += 1
            individual_users.append(set())
        else:
            individual_users[user].add(c)
    groups.append(len(set.intersection(*individual_users)))

print(sum(groups))
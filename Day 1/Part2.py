with open('Day1.txt', 'r') as f:
    lines = [line.strip().split() for line in f.readlines()]

team1 = []
team2 = []

for line in lines:
    team1.append(line[0])
    team2.append(line[1])

team1 = sorted(team1)
team2 = sorted(team2)

count = 0
final = 0
found = False
for i in range(len(team1)):
    for o in range(len(team2)):
        if team2[o] == team1[i]:
            found = True
            count += 1
        elif found == True and team2[o] > team1[i]:
            found = False
            final = final + (count * int(team1[i]))
            count = 0
            break
print(final)

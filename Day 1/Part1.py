with open('Day1.txt', 'r') as f:
    lines = [line.strip().split() for line in f.readlines()]

team1 = []
team2 = []

for line in lines:
    team1.append(line[0])
    team2.append(line[1])

team1 = sorted(team1)
team2 = sorted(team2)

total = 0

for i in range(len(team1)):
    if team1[i] > team2[i]:
        temp = int(team1[i]) - int(team2[i])
    else:
        temp = int(team2[i]) - int(team1[i])
    total = total + temp
print(total)


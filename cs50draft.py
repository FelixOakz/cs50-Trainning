import csv
teams = []
# TODO: Read teams into memory from file

with open('2018m.csv') as file:
	reader = csv.DictReader(file)
	for team in reader:
		team['rating'] = int(team['rating'])
		teams.append(team)

print(teams)
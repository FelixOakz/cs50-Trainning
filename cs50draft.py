import csv

teams = []
# reading teams from csv file and converting it to a dictionary inside teams list, while casting rating to integer

with open('2018m.csv') as file:
	reader = csv.DictReader(file)
	for team in reader:
		team['rating'] = int(team['rating'])
		teams.append(team)

for i in teams:
	print(i)
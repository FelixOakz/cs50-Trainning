import sys

names = ['Felix', 'Maria', 'Wilma', 'Vic', 'Bia']

if 'Bob' in names:
	print('Found')
	sys.exit(0)

print('Not found')
sys.exit(1)

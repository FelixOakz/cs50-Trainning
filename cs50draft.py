text = str(input('Text: '))
letters = 0
for i in range(len(text.replace(' ', ''))):
	if i != " ":
		letters += 1
print(text)
print(letters)

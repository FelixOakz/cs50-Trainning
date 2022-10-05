# accept text as string from user
text = str(input('Text: '))
letters = sentences = 0
words = 1

#counting leters, using isalpha function from cs50 manuals
for i in range(len(text)):
	if i != " ":
		text = text.replace(' ', '')
		letters += 1
	elif i == ' ':
		words += words
	elif '!' in i or '?' in i or '.' in i:
		sentences += sentences

# using given formula to calculate score
S = int(sentences / words * 100)
L = int(letters / words * 100)
grade = 0.0588 * L - 0.296 * S - 15.8
# printing result according to computed score
print(letters, sentences, words)
if grade < 1:
	print('Before grade 1.')
elif grade > 16:
	print('Grade 16+.')
else:
	print(f'Grade {grade}.')
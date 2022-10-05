quarters = dimes = nickels = pennies = total = 0
while True:
    value = int(input("Total value of change owed: "))
    while value >= 50:
        value -= 50
        quarters += 1
        total += 1
    while value >= 20:
        value -= 20
        dimes += 1
        total += 1
    while value >= 10:
        value -= 10
        nickels += 1
        total += 1
    while value >= 1:
        value -= 1
        pennies += 1
        total += 1
    break
print(total)
if quarters != 0:
    print(f'{quarters} notas de R$50,', end='')
if dimes != 0:
    print(f' {dimes} notas de R$20,', end='')
if nickels != 0:
    print(f' {nickels} notas de R$10,', end='')
if pennies != 0:
    print(f' {pennies} notas de R$1. Bom dia!')
name = input('')
fixedSalary = float(input(''))
salesTotal = float(input(''))

calc = ((salesTotal * 15) / 100) + fixedSalary

print('TOTAL = R$ {:.2f}'.format(calc))
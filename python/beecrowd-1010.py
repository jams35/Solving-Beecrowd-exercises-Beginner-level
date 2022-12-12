line1 = input().split(" ")

line2 = input().split(" ")

code_p1, numberUnits_p1, price_p1 = line1

code_p2, numberUnits_p2, price_p2 = line2

PAY = int(numberUnits_p1) * float(price_p1) + (int(numberUnits_p2) * float(price_p2))

print('VALOR A PAGAR: R$ {:.2f}'.format(PAY))

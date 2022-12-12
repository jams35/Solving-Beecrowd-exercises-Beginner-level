line1 = input().split(" ")

A, B, C = line1

areaTriangle = (float(A) * float(C)) / 2
areaCircle = 3.14159 * (float(C)**2)
areaTrapezium = ((float(A) + float(B)) * float(C) ) / 2
areaSquare = float(B) * float(B)
areaRectangle = float(A) * float(B)

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(areaTriangle, areaCircle, areaTrapezium,areaSquare, areaRectangle))


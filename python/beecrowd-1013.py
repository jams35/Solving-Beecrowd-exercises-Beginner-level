line1 = input().split(' ')

a, b, c = line1

maior1= (int(a) + int(b) + abs(int(a) - int(b))) / 2
maior2= (int(maior1) + int(c) + abs(int(maior1) - int(c))) / 2

print('{:.0f} eh o maior'.format(maior2))




import math

p1 = input().split(' ')
p2 = input().split(' ')

x1 , y1 = p1
x2 , y2 = p2

distance = math.sqrt(math.pow(float(x2)-float(x1), 2) + (math.pow(float(y2)-float(y1), 2)))


math.pow(distance,2)

print('{:.4f}'.format(distance))

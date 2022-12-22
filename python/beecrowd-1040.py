line1 = input().split(' ')

n1, n2, n3, n4 = line1

average = ((float(n1) * 2) + (float(n2) * 3) + (float(n3)*4) + (float(n4)*1)) /10

if average >= 7:
    print('Media: {:.1f}\nAluno aprovado.'.format(average))
if average == 5 and average <= 6.9:
    ne= float(input())
    print('Nota do exame: {}'.format(ne))
    if ne >= 7:
    
    
    # print('Media: {:.1f}\nAluno reprovado.'.format(average))

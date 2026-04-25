
numbers = [11,22,33,44,55,66,77,88,99]

for number in numbers:
    print(number%10, end= '\t')


numbers = {11,22,33,44,55,66,77,88,99}

for number in numbers:
    print(number%10, end= '\t')

stud = {'rno':101, 'name':'AAA','city': 'MUM'}

for k,v in stud.items():
    print(k,'--', v)

#functions
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
   return n1 * n2


def div():
    pass






#driver
num1=int(input('Enter a number :'))
num2=int(input('Enter another number :'))

res = add(num1, num2)
res = sub(num1, num2)
res =  mul(num1, num2)
print('Add:', res)
print('Sub:', res)
print('Mul:', res)

#ARBITARY
def add(nums):
    sum=0
    for n in nums:
        sum += n
    return sum




numbers = list()
count = int(input('How many ?'))

for _ in range(1, count+1):
    numbers.append(int(input('No: ')))
print(add(numbers))

#lambda

number = [1,2,3,4,5]
sq = lambda nums : [num * num for num in nums ]
print(tuple(sq(number)))
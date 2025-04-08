name = input('Type your name: ')

print('-'*40)

print('Nice to meet you, {:<20}!'.format(name))
print('Nice to meet you, {:^20}!'.format(name))
print('Nice to meet you, {:>20}!'.format(name))

print('-'*40)

print('Nice to meet you, {:=<20}!'.format(name))
print('Nice to meet you, {:=^20}!'.format(name))
print('Nice to meet you, {:=>20}!'.format(name))

print('-'*40)

n1 = int(input('Type a number: '))
n2 = int(input('Type a number: '))

sum = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
divInt = n1 // n2
pow = n1**n2

print('-'*40)

print('Sum: {}\nSub: {}\nMul: {}'.format(sum,sub,mul), end='')
print('\nDiv: {:.3f}\nDivInt: {}\nPow: {}'.format(div,divInt,pow))
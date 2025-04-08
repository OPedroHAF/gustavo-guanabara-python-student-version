
opt = ''

#-----------------------------------------------------------------------------------------

#FUNCTIONS
def printTable(n1,n2):
    count = 1
    while n1 <= n2:
        while count <= 10:
            print('{} x {} = {}'.format(n1, count, n1 * count))
            count += 1
        print('-' * 20)
        n1 += 1
        count = 0
    print('Completed')
#-----------------------------------------------------------------------------------------

n1 = int(input('Type a value to start showing the table: '))
while ((len(opt) < 1 or len(opt) > 1) or opt != 'Y' and opt != 'N'):
    opt = str.upper(input('Do you want to limit the range of the multiplications on every iteration? (Y/N)'))
match opt:
    case 'Y':
        n2 = int(input('Type a value to limit the table: '))
        printTable(n1,n2)
    case 'N':
        n2 = 10
        printTable(n1,n2)






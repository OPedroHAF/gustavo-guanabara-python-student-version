days = int(input('Amount of days on rent: '))
km = float(input('Kilometers droven: '))

finalValue = 60 * days + 0.15 * km

print('Final price: {:.2f}'.format(finalValue))
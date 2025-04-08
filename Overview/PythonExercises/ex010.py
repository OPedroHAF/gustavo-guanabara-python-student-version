productOriginalPrice = float(input('Type the price of the product: '))
productTenDiscountPrice = productOriginalPrice * 0.10
productInInstallmentsWithInterest = productOriginalPrice + (productOriginalPrice * 8/100)

print('Original price: {:.2f}\n10% discount: {:.2f}\nIn installments with interest of 8%: {:.2f}'.format(productOriginalPrice, productOriginalPrice - productTenDiscountPrice, productInInstallmentsWithInterest))
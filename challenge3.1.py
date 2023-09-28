gtdef LinearProductSearch(productList,targetProduct):
    listtest = []

    for index,product in enumerate(productList):
        if product == targetProduct:
            listtest.append(index)
    
    return listtest

products = ['shoes','boot','lofer','shoes','sandal','shoes']
target = 'shoes'
target1 = 'apple'
print(LinearProductSearch(products,target1)) 
stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ), ('EK', 300, '2-may-2002', 64), ('CAT', 44, '3-march-2001', 72) ]


purchases_report = [f'{purchase[0]}: {purchase[1]*purchase[3]}' for purchase in purchases]

for purchase in purchases_report:
    print(purchase)

totals = {}
for i in purchases:
    if i[0] in totals:
        totals[i[0]] += (i[1]*i[3])
    else:
         totals[i[0]] = (i[1]*i[3])

for i in totals:
    print(f'{i}: {totals.get(i)}')


# dict_1={'modelo' : ['marca', stock]}

productos = {
    'ASUS' : [
            'ASUS_110', 10,
            'ASUS_220', 5,
    ],
    'HP' : [
            'HP_110', 1,
            'HP_220', 2
    ]
}

key=input('INGRESA LA MARCA A CONSULTAR: ')
if key.upper() in productos:
    stock_i=0
    for i in productos[key[1]]:
        stock_total=stock_i+productos[key[i]]
    print(f'stock total: {stock_total}')
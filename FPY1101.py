from os import system
import time

productos = {
    'ASUS_110' : {'MARCA' : 'ASUS', 'STOCK' : 10},
    'ASUS_220' : {'MARCA' : 'ASUS', 'STOCK' : 5},
    'HP_110' : {'MARCA' : 'HP', 'STOCK' : 3}
}

precios = {
    'ASUS_110' : 550000,
    'ASUS_220' : 750000,
    'HP_110' : 330000
}

def iniciar():
    'Limpia el terminal'
    system('cls')

def stock_marca(marca:str):
    while True:
        try:
            sum(
                valor['STOCK']
                for valor in productos.values()
                if valor['MARCA']==marca
                )
        except:
            iniciar()
            print('NO SE CUENTA CON PRODUCTOS DE ESA MARCA')
            time.sleep(3)

def busqueda_precio(p_min, p_max):
    if precios[] in range(p_min, p_max)
        pass

def actualizar_precio(modelo, p):
    modelo = input('INGRESA EL MODELO:\n> ')
    if modelo not in precios:
        print('MODELO NO EXISTE')
    else:
        p=input('INGRESA EL NUEVO VALOR:\n> ')
        precios[modelo] = p
        print('\nEL PRECIO DEL PRODCUTO SE ACTUALIZÓ DE MANERA CORRECTA')
        time.sleep(3)
        iniciar()

def menu():
    while True:
        iniciar()
        print('--- MENÚ PRINCIPAL ---')
        print('\n1. STOCK MARCA')
        print('2. BÚSQUEDA POR PRECIO')
        print('3. ACTUALIZAR PRECIO')
        print('4. SALIR\n')
        ans=input('SELECCIONA UNA OPCIÓN:\n> ')
        match ans:
            case '1':
                while True:
                    iniciar()
                    marca=input('INGRESA LA MARCA A REVISAR:\n> ').upper()
                    stock_marca(marca)
            case '2':
                iniciar()
                p_min=('INGRESA EL PRECIO MÍNIMO:\n> ')
                p_max=('INGRESA EL PRECIO TOPE:\n> ')
                busqueda_precio(p_min, p_max)
            case '3':
                iniciar()
                actualizar_precio(modelo, p)
            case '4':
                iniciar()
                print('\nFINALIZANDO PROGRAMA')
                time.sleep(3)
                break
            case _:
                iniciar()
                print('\nOPCIÓN INVÁLIDA')
                time.sleep(3)

menu()

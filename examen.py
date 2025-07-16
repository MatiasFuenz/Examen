productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
            }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
        }

#Primer cambio o commit.

def menu():
    print('***MENU PRINCIPAL***')
    print('1.- Stock marca.')
    print('2.- Busqueda de precio.')
    print('3.- Listado de productos.')
    print('4.- Salir.')

def stock_marca():
    marca=input('Ingrese marca a consultar: ').capitalize().upper()
    for clave,dato in productos.items():
        if marca == dato[0]:
            print(clave, dato[0])
    for modelo,nomb in stock.items():
        print(nomb[1])
        if dato[0] == modelo:
            print(nomb[1])




def busqueda_precio(p_min,p_max):
    pass
    p_min = input('Ingrese precio minimo: ')
    p_max = input('Ingrese precio maximo: ')
    for modelo,dato in stock.items():
        if p_min >= dato[0] and p_max <= dato[0]:
            print(f'Los notebooks entre los precios consultas son: {dato[0]} -- {modelo}')

def ordenar_productos():
    print('-------Listado de Notbooks Ordenados----------')
    for modelo,dato in productos.items():
        print(f'{dato[0]} - {modelo} - {dato[2]} {dato[3]} - {dato[4]} ')

#'marca'-'modelo'-'ram'-'disco gb o t'    



#main
while True:
    menu()
    opc = input('Ingrese opción: ')
    if opc == '1':
        stock_marca()
    elif opc == '2':
        busqueda_precio()
    elif opc == '3':
        ordenar_productos()
    elif opc == '4':
        print('Programa finalizado.')
        break
    else:
        print('Debe seleccionar una opcion válida!!. ')
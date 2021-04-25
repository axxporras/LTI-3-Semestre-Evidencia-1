import pandas as pd
import datetime

directorio = {}
clavos = 20
martillo = 30
taladro = 50
respuesta = ''


while respuesta !=4:
    print('\nDetalle de Ventas Ferretería Don Alberto \n')
    print('[1] Registrar Venta(s)')
    print('[2] Consultar Venta(s)')
    print('[3] Encontras Venta(s) por fecha')
    print('[4] Salir')
    respuesta = int(input('\n'))
    
    if respuesta ==1:
        ventas = int(input('\nNúmero de ventas realizadas: \n'))
        precio = []
        
        for numero in range(ventas):
            print('\nSeleccione el artículo vendido: \n')
            print('[1] Caja de Clavos')
            print('[2] Martillo')
            print('[3] Taladro')
            articulo = int(input('\n'))
                
            if articulo ==1:
                unidades= int(input('\nUnidades vendidas: \n'))
                costo= clavos*unidades
                fecha = input('\nIngrese la fecha de hoy (YYYY-MM-DD): \n')
                directorio[fecha] = ['Caja de clavos', unidades, costo]
                precio.append(costo)
                
            
            elif articulo ==2:
                unidades= int(input('\nUnidades vendidas: \n'))
                costo= martillo*unidades
                fecha = input('\nIngrese la fecha de hoy (YYYY-MM-DD): \n')
                directorio[fecha] = ['Martillo', unidades, costo]
                precio.append(costo)
                
            elif articulo ==3:
                unidades= int(input('\nUnidades vendidas: \n'))
                costo= taladro*unidades
                fecha = input('\nIngrese la fecha de hoy (YYYY-MM-DD): \n')
                directorio[fecha] = ['Taladro', unidades, costo]
                precio.append(costo)
            
        preciofinal= sum(precio)
        print(f'\nEl precio total de compra es de {preciofinal} pesos \n')
        print('--Devuelta al menú-- \n')
                
                
                
            
            
    
    elif respuesta ==2:
        print('\nDirectorio de Ventas \n')
        print(directorio)
        print('\n--Devuelta al menú-- \n')
        
            
    elif respuesta ==3:
        fecha_buscar = (input('Introduzca fecha (YYYY-MM-DD): '))
        if fecha_buscar in directorio.keys():
            print(directorio[fecha])
        else:
            print('No hay ninguna venta registrada ese día')
            print('\n--Devuelta al menú-- \n')
            
    elif respuesta ==4:
        datadirectorio = pd.DataFrame(directorio)
        datadirectorio.index = ["Articulo", "Unidades", "Costo"]
        datadirectorio.to_csv (r'directorio.csv',index=True, header=True)
        print('\nGracias, vuelva pronto \n')
                
            
    
    
    

    

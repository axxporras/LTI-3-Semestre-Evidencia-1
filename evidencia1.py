directorio = []
clavos = 20
martillo = 30
taladro = 50
respuesta = ''


while respuesta !=3:
    print('\nDetalle de Ventas Ferretería Don Alberto \n')
    print('[1] Registrar Venta(s)')
    print('[2] Consultar Venta(s)')
    print('[3] Salir')
    respuesta = int(input('\n'))
    
    if respuesta ==1:
        ventas = int(input('\nNúmero de ventas realizadas: \n'))
        precio = []
        
        for numero in range(ventas):
            registro = []
            print('\nSeleccione el artículo vendido: \n')
            print('[1] Caja de Clavos')
            print('[2] Martillo')
            print('[3] Taladro')
            articulo = int(input('\n'))
                
            if articulo ==1:
                unidades= int(input('\nUnidades vendidas: \n'))
                costo= clavos*unidades
                registro.append('Caja de clavos')
                registro.append(f'{unidades} unidades')
                registro.append(f'${costo}')
                directorio.append(registro)
                precio.append(costo)
                
            
            elif articulo ==2:
                unidades= int(input('\nUnidades vendidas: \n'))
                costo= martillo*unidades
                registro.append('Martillo')
                registro.append(f'{unidades} unidades')
                registro.append(f'${costo}')
                directorio.append(registro)
                precio.append(costo)
                
            elif articulo ==3:
                unidades= int(input('\nUnidades vendidas: \n'))
                costo= taladro*unidades
                registro.append('Taladro')
                registro.append(f'{unidades} unidades')
                registro.append(f'${costo}')
                directorio.append(registro)
                precio.append(costo)
            
        preciofinal= sum(precio)
        print(f'\nEl precio total de compra es de {preciofinal} pesos \n')
        print('--Devuelta al menú-- \n')
                
                
                
            
            
    
    elif respuesta ==2:
        print('\nDirectorio de Ventas \n')
        if directorio:
            for elemento in directorio:
                print(elemento)
            print('\n--Devuelta al menú-- \n')
        
        else:
            print('\nNo se han registrado ventas \n')
            print('--Devuelta al menú-- \n')
            
    elif respuesta ==3:
        print('\nGracias, vuelva pronto \n')
                
            
    
    
    

    

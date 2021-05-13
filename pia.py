import sqlite3
import datetime

labial = 20
sombra = 15
delineador = 40
treinta = [4, 6, 9, 11]
respuesta = ''
fechadehoy = datetime.datetime.now()
añoactual = int(fechadehoy.strftime('%Y'))


conexion = sqlite3.connect('ventas.db')
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Ventas " \
               "(Descripcion VARCHAR(100), PiezasVendidas VARCHAR(100), Precio SMALLINT(10), Fecha timestamp)")

conexion.commit()

while respuesta !=3:
    try:
        print('\nDetalle de Ventas *Cosmeticos Filomena* \n')
        print('[1] Registrar una Venta')
        print('[2] Realizar Consulta')
        print('[3] Salir')
        respuesta = int(input('\n'))
        
        if respuesta==1:
            try:
                print('\nArtículo vendido: \n')
                print('[1] Lapiz Labial')
                print('[2] Sombra de Ojos')
                print('[3] Delineador')
                articulo = int(input('\n'))
                
                if articulo==1:
                    try:
                        unidades = int(input('\nPiezas vendidas: \n'))
                        piezas = str(unidades)                        
                        y = fechadehoy.year
                        m = fechadehoy.month
                        d = fechadehoy.day
                        fecha = datetime.datetime(y, m, d)
                        valores = ('Lapiz Labial', piezas, labial, fecha)
                        
                        cursor.execute("INSERT INTO Ventas(Descripcion, PiezasVendidas, Precio, Fecha) VALUES(?, ?, ?, ?)", valores)                    
                        conexion.commit()
                                       
                                       
                        
                        monto = labial*unidades
                        print('Se ha registrado la venta')
                        print(f'\nEl monto total fue de {monto} pesos \n')
                        print('Devuelta al menu.')
                        
                        
                    
                    except ValueError:
                        print("Accion invalida. Devuelta al menu.")
                
                elif articulo==2:
                    try:
                        unidades = int(input('\nPiezas vendidas: \n'))
                        piezas = str(unidades)
                        date = datetime.datetime.now()
                        y = date.year
                        m = date.month
                        d = date.day                        
                        fecha = datetime.datetime(y, m, d)
                        valores = ('Sombra de Ojos', piezas, sombra, fecha)
                        
                        cursor.execute("INSERT INTO Ventas(Descripcion, PiezasVendidas, Precio, Fecha) VALUES(?, ?, ?, ?)", valores)                    
                        conexion.commit()
                                       
                                       
                        
                        monto = sombra*unidades
                        print('Se ha registrado la venta')
                        print(f'\nEl monto total fue de {monto} pesos \n')
                        print('Devuelta al menu.')
                        
                    
                    except ValueError:
                        print("Accion invalida. Devuelta al menu.")
                
                elif articulo==3:
                    try:
                        unidades = int(input('\nPiezas vendidas: \n'))
                        piezas = str(unidades)
                        date = datetime.datetime.now()
                        y = date.year
                        m = date.month
                        d = date.day
                        fecha = datetime.datetime(y, m, d)
                        valores = ('Delineador', piezas, delineador, fecha)
                        
                        cursor.execute("INSERT INTO Ventas(Descripcion, PiezasVendidas, Precio, Fecha) VALUES(?, ?, ?, ?)", valores)                    
                        conexion.commit()
                                       
                                       
                        
                        monto = delineador*unidades
                        print('Se ha registrado la venta')
                        print(f'\nEl monto total fue de {monto} pesos \n')
                        print('Devuelta al menu')
                        
                    
                    except ValueError:
                        print("Accion invalida. Devuelta al menu.")
                
                else:
                    print("Accion invalida. Devuelta al menu.")
            
            except ValueError:
                print("Accion invalida. Devuelta al menu.")
            
        elif respuesta==2:
            try:
                año= int(input('\nIngrese el año de la venta: \n'))
                año1= str(año)
                if len(año1)<4:
                    print("Accion invalida. Devuelta al menu.")
                elif año>añoactual:
                    print("Accion invalida. Devuelta al menu.")
                else:
                    try:
                        mes= int(input('\nIngrese el mes de la venta: \n'))
                        mes1= str(mes)
                        if len(mes1)>2:
                            print("Accion invalida. Devuelta al menu.")
                        elif mes>12:
                            print("Accion invalida. Devuelta al menu.")
                        else:
                            try:
                                dia= int(input('\nIngrese el dia de la venta: \n'))
                                dia1 = str(dia)
                                if len(dia1)>2:
                                    print("Accion invalida. Devuelta al menu.")
                                elif dia>31:
                                    print("Accion invalida. Devuelta al menu.")
                                elif dia>30 and mes in treinta:
                                    print("Accion invalida. Devuelta al menu.")
                                elif dia>29 and mes==2:
                                    print("Accion invalida. Devuelta al menu.")
                                else:                                    
                                    fecha1 = datetime.datetime(año, mes, dia)
                                    print(fecha1)
                                    cursor.execute("SELECT * FROM Ventas WHERE Fecha = ?", (fecha1,))
                                    ventas = cursor.fetchall()
                                    
                                    if not ventas:
                                        print("No hay ninguna venta registrada. Devuelta al menu.")
                                    
                                    else:
                                        print("{:>10} {:>8} {:>2} {:>2}".format( 
                                        "DESCRIPCION",
                                        "PIEZAS",
                                        "PRECIO",
                                        "FECHA"))
                                        print('')
                                        for venta in ventas:                                        
                                            print(venta)
                                        
                                        print("Devuelta al menu.")
                                     
                                
                                
                            
                            except ValueError:
                                print("Accion invalida. Devuelta al menu.")
                                
                    
                    except ValueError:
                        print("Accion invalida. Devuelta al menu.")
                                              
                                  
            except ValueError:
                print("Accion invalida. Devuelta al menu.")
                         
            
        elif respuesta==3:
            print('\nGracias, vuelva pronto \n')
            conexion.close()
        
        else:
            print("Accion invalida. Devuelta al menu.") 
    
    
    except ValueError:
        print("Accion invalida. Devuelta al menu.")


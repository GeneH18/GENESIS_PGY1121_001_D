import os
import numpy as np
import funcionesEdificio as fn
edificio = np.empty([10,4], type(int))
fn.llenarMatriz(edificio)
os.system("cls")
op=0
departamento=0
while(op!=5):
    os.system("cls")
    print( " **********************")
    print( " ***   CASA FELIZ   ***")
    print( " 1. Comprar departamento" )
    print( " 2. Mostrar departamentos disponibles")
    print( " 3. Ver listado de compradores")
    print( " 4. Mostrar ganancias totales")
    print( " 5. Salir")
    print("  **********************")
    op=int(input( " Elija una opción entre 1 y 5 "))
    while(True):
        try:
            op=int(input(" Elija opción: "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar opción entre 1 y 5")
        except ValueError:
            print("Debe ser un número entero")
        if(op==1):
            fn.validarRut
            fn.validarPiso
        if(op==2):
            fn.buscarDisponible
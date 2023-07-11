import os
import random
import numpy as np
op=0
def llenarMatriz(mat):
    os.system("cls")
    for i in range(10):
        for j in range(4):
            mat[i,j]=" "

def validarRut(rut):
    while(True):
        try:
            rut=int(input(" Ingrese su Rut "))
            if(rut <= 8):
                break
            else:
                print("Debe tener mínimo 8 caracteres")
        except ValueError:
            print("Debe ser un número entero")
    return rut
                             
def validaOpcion(op):
    while(True):
        try:
            op=int(input(" Elija opción: "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar opción entre 1 y 5")
        except ValueError:
            print("Debe ser un número entero")
    return op

def mostrarDisponibles(departamento):
    os.system("cls")
    for i in range(10):
        print("\n")
        for j in range(4):
            if(j==1):
                print("\t",departamento[i,j], end="      " )
            else:
                print("\n",departamento[i,j], end="   ")
    print("\n\n")

def validarPiso(piso):
    piso=0
    while True:
        try:
            piso=int(input(" Ingrese un piso del 1 al 10 "))
            if(piso>=1 and piso<=10):
                break
            else:
                print(" Debe ingresar un piso entre 1 y 10 ")
        except ValueError:
            print(" Debe ser un piso entre 1 y 10")
    return piso

def buscarDisponible(piso, TipoDepartamento):
    for i in range(10):
        for j in range(4):
            if (piso==TipoDepartamento[i,j]):
                return True
    return False 


    



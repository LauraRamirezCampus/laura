#laura ramirez
#prueba tipo reto
def validarEntero(etiqueta):
    while True:
        try:
            valor=int(input(etiqueta))       
            break
        except ValueError:
            print("el valor ingresado debe ser un numero entero")
    return valor

def validaTipo():
    while True:
        try:   
            tipo=int(input("ingrese el tipo de IVA, que puede ser \n1: Exento de IVA,\n2: Bienes, donde se aplica como IVA el 5%,\n3: General, donde se aplica como IVA el 19%:"))
            if tipo<1 or tipo>3:
                print("el valor ingresado debe estar entre 1 a 3")
                continue
            break
        except ValueError:
            print("el valor ingresado debe ser un numero entero")
    return tipo

def calcularIva(tipo,valU):
    if tipo==1:
        iva=0
    elif tipo==2:
        iva=0.05
    else:
        iva=0.19
    totalu=(valU*cant)
    valorIva=(valU*iva)
    valorP=totalu+valorIva
    valorFi=valU+valorIva
    return iva,totalu,valorIva,valorFi,valorP

valTotal=0
cantC=0
clientesM=0
clientesH=0
valtp=0 #contador para el valor de la venta de todos los productos
valTi=0#sumador para el valor total del IVA
valTsI=0#el valor de la venta de los productos sin IVA.
N=validarEntero("ingrese cantidad de clientes que realizan compras durante en día: ")
for i in range(N):
    cc=input("ingrese la cedula: ")
    nom=input("ingrese el nombre del cliente: ")
    sexo=input("ingrese el sexo(F: Femenino, M:Másculino): ")
    M=validarEntero("ingrese la cantidad de productos comprados: ")
    for j in range(M):
        cod=input("Ingrese el código del producto: ")
        valU=validarEntero("Ingrese el valor unitario del producto: ")
        cant=validarEntero("Ingrese la cantidad comprada:")
        tipo=validaTipo()
        iva,totalu,valorIva,valorFi,valorP=calcularIva(tipo,valU)
        valTotal+=valorFi
        print("\nEl valor del producto es: ",totalu,"\nEl valor del iva es: ",valorIva,"\nEl valor final es: ",valorFi,"\n")
    if sexo=="F":
        clientesM+=1
    elif sexo=="M":
        clientesH+=1  
    valtp+=valorP
    valTi+=valorIva
    valTsI+=totalu

print("\nEn el dia se tuvo: ",N," clientes \nFueron ",clientesM,"mujeres \nFueron ",clientesH,"hombres ")
print("El valor de la venta de todos los productos: ",valtp)
print("el valor total del IVA: ",valTi)
print("el valor de la venta de los productos sin IVA: ",valTsI)
    

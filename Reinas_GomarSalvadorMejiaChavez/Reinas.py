#############################################
#          Gomar Salvador Juan Manuel       #
#          Mejía Chávez María Fernanda      #
#############################################

print('#----- R E I N A S-------#')
print()

matriz =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#guarda posicion 
posAct=[]
llave = 0

posiciones = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def entrada(num_reinas, matriz, llave,posiciones):
    contened = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    cont = 0
    print("num_reinas "+str(num_reinas))
 
    if num_reinas == 1:
        return solucion(matriz)
    else: 
        for i in range(len(matriz)):
            for r in range(len(matriz[i])):
                
                if cont == 0:
					
                    if posiciones[i][r] != 3:
                        if(matriz[i][r] == 0):

                            if num_reinas == 4:
                                posiciones[i][r] = 3
                            matriz[i][r] = 1
                            cont = cont + 1
                            posAct.append([i,r])

        matriz = iterar(matriz,posAct)

        posAct.pop(0)
        for i in matriz:

            if 0 in i:
                llave = 0
            else:
                llave = 1
        if llave == 1:
            print(llave)
            for i in contened:
                print(i)
            num_reinas=4
            llave=0
            return entrada(num_reinas,contened,llave,posiciones)
        if llave == 0:
            print(llave)
            num_reinas=num_reinas-1
            return entrada(num_reinas,matriz,llave,posiciones)

def iterar(matriz,posAct):
    print("###Rev de diagonales verticales y horizontales####")
    a = posAct[0][0]
    b = posAct[0][1]
    r = range(len(matriz))
    b2 = b
    b1 = a
    print(posAct)
    
    for i in range(len(matriz)):
        for r in range(len(matriz[i])):
            matriz[a][r] = 2
            matriz[i][b] = 2
    imp(matriz)
    for i in range(len(matriz)):
        b2 = b2-1
        b1 = b1 -1
        if (b2 >= 0)and(b1 >=0):
            print("- -")
            matriz[b1][b2] = 2
    b2 = b
    b1 = a
    imp(matriz)
    for i in range(len(matriz)):
        b1 = b1 +1
        b2 = b2 +1
        if (b1 <= r)and(b2 <= r):
            print("+ +")
            matriz[b1][b2] = 2

    b2 = b
    b1 = a
    imp(matriz)
    for i in range(len(matriz)):
        b2 = b2+1
        b1 = b1 -1
        if (b2 < r)and(b1 >=0):
            print("+ -")
            matriz[b1][b2] = 2
    b2 = b
    b1 = a
    imp(matriz)
    for i in range(len(matriz)):
        b2 = b2-1
        b1 = b1 + 1
        if (b2 >= 0)and(b1 <r):
            print("- +")
            matriz[b1][b2] = 2
    matriz[a][b]=1
    imp(matriz)
    print("############")
    return matriz
    

def solucion(matriz):
    for i in range(len(matriz)):
        for r in range(len(matriz[i])):
            if (matriz[i][r]) == 0:
                 matriz[i][r] = 1
    print()
    print('#---R E S U L T A D O---#')
    for i in matriz:
        print(i)

def imp(matriz):
    print("############")
    for i in matriz:
        print(i)

entrada(4,matriz,0,posiciones)

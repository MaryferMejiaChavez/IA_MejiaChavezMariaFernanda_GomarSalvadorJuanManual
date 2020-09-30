#############################################
#          Gomar Salvador Juan Manuel       #
#          Mejía Chávez María Fernanda      #
#############################################

Tin = [
        ("tortuga","garras"),
        ("tortuga","Proteccion queratina"),
        ("gallo","garras"),
        ("gallo","Proteccion queratina"),
        ("cocodrilo","garras"),
        ("cocodrilo","Proteccion queratina"),
        ("iguana","garras"),
        ("iguana","Proteccion queratina"),
        ("gato","g. mamarias"),
        ("gato","pelo"),
        ("gato","garras"),
        ("oso","g. mamarias"),
        ("oso","pelo"),
        ("oso","garras"),
        ("ballena","g. mamarias"),
        ("ballena","pelo"),
        ("delfin","g. mamarias")
        ]
Viv = [
        ("tortuga","agua"),
        ("cocodrilo","agua"),
        ("ballena","agua"),
        ("delfin","agua"),
        ("tortuga","tierra"),
        ("iguana","tierra"),
        ("gallo","tierra"),
        ("gato","tierra"),
        ("oso","tierra")
       ]

Ser = [
        ("tortuga","Sauropsido"),
        ("gallo","Sauropsido"),
        ("cocodrilo","Sauropsido"),
        ("iguana","Sauropsido"),
        ("gato","mammalia"),
        ("ballena","mammalia"),
        ("oso","mammalia"),
        ("delfin","mammalia"),

        ("mammalia","viviparo"),
        ("viviparo","tetrapodo"),
        ("Sauropsido","oviparo"),
        ("oviparo","tetrapodo"),
        ("tetrapodo","vertebrado")
       ]


def Tiene(A,B,Ti):
    if not Ti:
        return False
    i = 0
    f = len(Ti)
    while i < f:
        if Ti[i][0] == A and Ti[i][1] == B:
            return True
        i = i + 1
    else:
        return False

def Vive(A,B,Vi):
    if not Vi:
        return False
    i = 0
    f = len(Vi)
    while i < f:
        if Vi[i][0] == A and Vi[i][1] == B:
            return True
        i = i + 1
    else:
        return False
                        
def Es(A,B,Se):
    if not Se:
        return False
    i = 0
    f = len(Se)
    while i < f:
        if Se[i][0] == A:
            if Se[i][1] == B:
                return True
            else:
                A = Se[i][1]
                i = -1
        i = i + 1
    else:
        return False
  
print (Tiene("cocodrilo","pelo",Tin))
print (Vive("gallo","agua",Viv))
print (Vive("tortuga","tierra",Viv))
print (Es("mammalia","oviparo",Ser))
print (Tiene("gato","garras",Tin))
print (Vive("tortuga","agua",Viv))
print (Es("mammalia","tetrapodo",Ser))

def esta(A,B,Vi):
    if not Vi:
        return False
    i = 0
    f = len(Vi)
    while i < f:
        if Vi[i][0] == A and Vi[i][1] == B:
            return True
        i = i + 1
    else:
        return False
def op1(A):
    def op2(B):
        def lista(Vi):
            return esta(A,B,Vi)
        return lista
    return op2
    
#          wrappers                       #

def Vive():
    return op1("tortuga")("agua")(Viv)
print("La tortuga vive en agua")
print(Vive())
def Tiene():
    return op1("cocodrilo")("pelo")(Tin)
print("El cocodrilo tiene pelo")
print(Tiene())
def Vive():
    return op1("gallo")("agua")(Viv)
print("El gallo vive en el agua")
print(Vive())
def Tiene():
    return op1("gato")("garras")(Tin)
print("El gallo tiene garras")
print(Tiene())
def Vive():
    return op1("tortuga")("tierra")(Viv)
print("La tortuga vive en tierra [algunas especies]")
print(Vive())
def Es():
    return op1("oviparo")("tetrapodo")(Ser)
print(Es())
def Es():
    return op1("mammalia")("oviparo")(Ser)
print(Es())

#from __future__ import print_function

def mi_funcion():
    print "Hola mundo"

mi_funcion()

a=mi_funcion()

print a


def nombres(nombre,apellido):
    #nombre_completo= nombre, apellido #Concatenacion como tupla
    #nombre_completo= nombre + apellido + str(edad) #Concatenacion como cadena
    nombre_completo="Mi nombre es %s %s y tengo %d" % (nombre, apellido)

    print nombre_completo


nombres("Luis ","Carrillo ")

a=100
b=501
c=a*b
print(c)


# Ejemplo a ser replicado
def add_one(x):
    return x+1
add_one(100001)

#Ejemplo 1, suma simple
x=lambda a: a+10
print(x(120))

#Ejemplo 2, multiplicación
x=lambda a,b:a*b
print(x(5,60))

#Ejemplo 3, conn cualquier número de argumentos
x=lambda a,b,c:a+b+c
print(x(5,6,20))


# Se añade la función lambda para ejemplo con strings

#Ejemplo con strings
full_name=lambda first,last: f'Full name:{first.title()} {last.title()}'
full_name('EBAC','Curso de Data Analysis')
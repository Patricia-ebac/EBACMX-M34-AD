#Generando una operación a ser aplicada a un listado de números
#listado de nuemros con exponencial

#Declara la lista
org_list=[1,2,3,4,5]
fin_list=[]

#Aplica la operación a cada uno de los números de la lista
for num in org_list:
    fin_list.append(num**3)

#Imprime la lista
print(fin_list)

#largo de cada elemento en una vista, con función 'len'
org_list=["Hey", "mundo","EBAC"]
fin_list=list(map(len,org_list))
print(fin_list)

import json
import csv

# Crear archivo hola.txt (write)
f = open('hola.txt','w')
# Escribir un archivo de Hola mundo
f.write('Hola Mundo\n')
# Cerrar conexión de archivos
f.close()

# Abrir archivo con with (append)
with open('hola.txt','a') as f:
	f.write('Prueba con with\n')	
	f.write('sigo escribiendo..')

# Leer archivo hola txt
f = open('hola.txt','r')
# Imprimir información de archivo
f.read()
f.close()

print('-----')
# Escribir archivo en json
d = {
	'alumnos':['Oscar','Oscar','Mauricio'],
	'semestre': 10,
	'facultad':'ingenieria'
}
# Escribir JSON
with open('json_ex.json','w') as f:
	json.dump(d,f)

# Cargar Diccionario con libreria de JSON
f = open('json_ex.json','r').read()
f_json = json.loads(f)
# Imprime Dict
print(f_json['alumnos'])
print(type(f_json))
# Imprime solo string
print(f)
print(type(f))

print('-----')
# Escribir en CSV
f = open('csv_ex.csv','w')
f.write('clase,alumno,semestre,calificacion\n')
lista= 'tsp,yo,10,10\n'
for i in range(10):
	f.write(lista)
f.close()

# Leer archivo
f = open('csv_ex.csv','r')
for x in csv.reader(f, delimiter=','):
	print(x)
f.close()

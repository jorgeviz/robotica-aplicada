# Importación de una Clase propia

# Tipo de importación completa
from clase import *

# Tipo de importación exclusiva
#from clase import MyClass

# Instanciación de una clase
c1 = MyClass(1)
c2 =MyClass(2)

# Llamado a atributos de un objeto
print(c1.g)

# Modificación de atributos 
c1.g = 3

# Llamada a métodos de Clase
print(c1.g, c1.velocidad, c1.add_v(2,2))
print(c2.g, c2.velocidad, c2.add_v(2,2))


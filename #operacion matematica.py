#OPERACION MATEMATICA
#Un tren sale de la estacion y realiza un recorrido a una velocidad de 100 km/h (supiniendo que la velocidad sea constante), calcular en cuantos minutos llega a los diferentes pueblos
import numpy as np
velocidad_tren= 100
distancia_pueblo1= 50
distancia_pueblo2= 100
distancia_pueblo3= 150
horario_llegada_pueblo1= (distancia_pueblo1*60)/velocidad_tren
horario_llegada_pueblo2= (distancia_pueblo2*60)/velocidad_tren
horario_llegada_pueblo3= (distancia_pueblo3*60)/velocidad_tren

print (f"El tren EXPRESO DEL PACIFICO llega al pueblo de SPRINGFIELD en {horario_llegada_pueblo1} minutos.")
print (f"El tren EXPRESO DEL PACIFICO llega al pueblo de WONDERLAND en {horario_llegada_pueblo2} minutos.")
print (f"El tren EXPRESO DEL PACIFICO llega al pueblo de NEVERLAND en {horario_llegada_pueblo3} minutos.")

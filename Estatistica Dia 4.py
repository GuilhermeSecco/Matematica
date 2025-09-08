import numpy as np
import pandas as pd

valores = [1.25, 3.75, 6.25, 8.75]
frequencia = [2, 3, 25, 10]

valor = []

for i in range(len(valores)):
    valor.append(valores[i] * frequencia[i])

media = (valor[0]+valor[1]+valor[2]+valor[3])/(frequencia[0]+frequencia[1]+frequencia[2]+frequencia[3])
media = round(media, 2)

variancia = ((((valores[0]-media)**2)*frequencia[0])+(((valores[1]-media)**2)*frequencia[1])+(((valores[2]-media)**2)*frequencia[2])+(((valores[3]-media)**2)*frequencia[3]))/((frequencia[0]+frequencia[1]+frequencia[2]+frequencia[3])-1)
variancia = round(variancia, 2)
print(variancia)

desvio = variancia**0.5
desvio = round(desvio, 2)
print(desvio)

coeficiente = (desvio/media)*100
coeficiente = round(coeficiente, 2)
print("O coeficiente de variação é de: "+ str(coeficiente)+ "%")
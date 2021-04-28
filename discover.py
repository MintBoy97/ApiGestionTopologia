#!/usr/bin/env python3
from module_scan import *

def maqueta_conexiones(interfaces,conexiones_pc):
    resultado = {}
    for i in interfaces:
        for x in i.keys():
            #Si es un router y no se han revisado sus conexiones directas se aplica el algoritmo
            if i[x][0] == 'R':
                # Agregamos el router para saber que ya lo escaneamos
                conexiones = []
                for j in interfaces:
                    for y in j.keys():
                        if x != y:
                            # Se itera en todos los dispositivos de la topología y encontramos los 
                            # saltos directos que tiene el router que vamos a analizar 
                            if j[y][0] == 'R' and i[x] != j[y]:
                                try:
                                    network = conexiones_router(x,y)
                                except:
                                    pass
                                else:
                                    # Si la conexion directa encontrada no esta en nuestra lista de ip's se agrega
                                    if network not in conexiones:
                                        conexiones.append(network)
                    conR = {"name":i[x],"conexiones": conexiones }
                    resultado[x]=conR
    resultado.update(conexiones_pc)
    return resultado
from module_scan import *
interfaces = [{'192.168.0.1': 'R0'}, {'192.168.0.10': 'Unix-OS 0'}, {'10.10.0.129': 'R0'}, {'10.10.0.130': 'R1'}, {'10.10.0.133': 'R1'}, {'10.10.0.134': 'R2'}, {'192.168.0.129': 'R2'}, {'192.168.0.137': 'Unix-OS 3'}, {'192.168.0.138': 'Unix-OS 3'}]


router_scaneados = []
resultado = {}
for i in interfaces:
    for x in i.keys():
        #Si es un router y no se han revisado sus conexiones directas se aplica el algoritmo
        if i[x][0] == 'R' and i[x] not in router_scaneados:
            # Agregamos el router para saber que ya lo escaneamos
            router_scaneados.append(i[x])
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
                                print("error")
                            else:
                                # Si la conexion directa encontrada no esta en nuestra lista de ip's se agrega
                                if network not in conexiones:
                                    conexiones.append(network)
                conR = {"name":i[x],"conexiones": conexiones }
                resultado[x]=conR

            

print(resultado)
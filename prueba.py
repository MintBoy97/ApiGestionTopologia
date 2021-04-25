#!/usr/bin/env python3
from module_scan import *
from topologia import Topologia
from discover import coneziones

# Listamos las interfaces de red aqui
interfaces=os.listdir("/sys/class/net/")
c=0
#for i in range(len(interfaces)):
#    print(f"{i+1}: {interfaces[i]}")
#read=int(input("Ingresa el numero de interfaz: "))-1
# Modulo que permite escanear todos los datos
recibidos, conexiones_pc = scan_by_interface('enp0s3',"admin","admin01","1234")
maquetado = coneziones(recibidos,conexiones_pc)
print(maquetado)
topo = Topologia(maquetado, "templates")
topo.print_rep_html_flask()
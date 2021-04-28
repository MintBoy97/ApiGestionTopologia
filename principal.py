from module_scan import os, scan_by_interface
from topologia import Topologia
from discover import maqueta_conexiones

def deteccionTopologia():
    # Listamos las interfaces de red aqui
    interfaces=os.listdir("/sys/class/net/")
    # Modulo que permite escanear todos los datos
    recibidos, conexiones_pc = scan_by_interface('enp0s3',"admin","admin01","1234")
    maquetado = maqueta_conexiones(recibidos,conexiones_pc)
    print(maquetado)
    topo = Topologia(maquetado, "templates")
    topo.print_rep_html_flask()
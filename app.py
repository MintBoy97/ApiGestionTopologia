from flask import Flask, render_template, url_for, flash, redirect
from module_scan import os, scan_by_interface
from topologia import Topologia
from discover import maqueta_conexiones

app = Flask(__name__)


@app.route('/')
@app.route('/inicio')
def home():
    # descubrimiento y visualizacion de topologia
    # Listamos las interfaces de red aqui
    interfaces=os.listdir("/sys/class/net/")
    # Modulo que permite escanear todos los datos
    recibidos, conexiones_pc = scan_by_interface('enp0s3',"admin","admin01","1234")
    maquetado = maqueta_conexiones(recibidos,conexiones_pc)
    #
    
    print('----------Conexiones encontradas de la siguiente manera-----------------')
    print(maquetado)
    topo = Topologia(maquetado, "templates")
    topo.print_rep_html_flask()
    
    return render_template('inicio.html')

@app.route('/info')
def about():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)
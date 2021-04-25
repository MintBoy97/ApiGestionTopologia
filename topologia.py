from pyvis.network import Network
import networkx as nx

class Topologia:

    # constructor
    def __init__(self,info_topologia,ruta_destino):
        self.grafo = nx.empty_graph()
        self.id_rot = 0
        self.id_swt = 0
        self.id_vpc = 0
        self.id_nodo = 0
        self.ruta_destino = ruta_destino
        # crear la nueva topologia
        elementos = {}
        for i in info_topologia.keys():
            elementos[info_topologia[i]['name']] = {'dir':[],'id':-1}
        for i in info_topologia.keys():
            ip = i
            elementos[info_topologia[i]['name']]['dir'].append(ip)
        for i in elementos.keys():
            if i[0] == 'R':
                elementos[i]['id'] = self._agrega_rot(nombre=i)
            else:
                elementos[i]['id'] = self._agrega_vpc(nombre=i)
        print(elementos)
        print(info_topologia)
        for i in info_topologia.keys():
            for j in info_topologia[i]['conexiones']:
                id = elementos[info_topologia[i]['name']]['id']
                id2 = elementos[info_topologia[j]['name']]['id']
                self._forma_con(id ,id2 )
                    
                    
                    

    
    def _agrega_rot(self,nombre="R",info="router",img="img/router.png"):
        # agrega un router al grafo
        self.grafo.add_node(self.id_nodo,size=20,title=info,label=nombre,group=1,image=img,shape='image')
        self.id_nodo += 1
        return self.id_nodo-1
    
    # agrega un switch al grafo
    def _agrega_swt(self,nombre="SW",info="switch",img="img/switch.png"):
        self.grafo.add_node(self.id_nodo,size=20,title=info,label=nombre,group=1,image=img,shape='image')
        self.id_nodo += 1
        return self.id_nodo-1
    
    # agrega una vpc al grafo
    def _agrega_vpc(self,nombre="PC",info="vpc",img="img/vpc.png"):
        self.grafo.add_node(self.id_nodo,size=20,title=info,label=nombre,group=1,image=img,shape='image')
        self.id_nodo += 1
        return self.id_nodo-1
    
    # forma una conexion entre dos nodos
    def _forma_con(self,nodo1,nodo2):
        self.grafo.add_edge(nodo1,nodo2,weight=5)

    # genera la representacion del grafo en formato html
    def print_rep_html(self):
        self.nt = Network('500px','500px')
        self.nt.from_nx(self.grafo)
        self.nt.save_graph(self.ruta_destino+"/topologia.html")

    # remplazar rutas locales por rutas estaticas del framework
    def print_rep_html_flask(self):
        self.print_rep_html()
        archivo = open(self.ruta_destino+"/topologia.html",'rb')
        cont_archivo = archivo.read()
        archivo.close()

        elementos = [b'router',b'switch',b'vpc']
        for elemento in elementos:
            cont_archivo = cont_archivo.replace(b"img/" + elemento + b".png",
            b"{{ url_for('static', filename='img/" + elemento + b".png') }}")
        
        cont_archivo = cont_archivo.replace(b"https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis.css",
        b"{{ url_for('static', filename = 'css/vis.css') }}")

        cont_archivo = cont_archivo.replace(b"https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis-network.min.js",
        b"{{ url_for('static', filename = 'js/vis-network.min.js') }}")

        nuevo_archivo = open(self.ruta_destino+"/topologia_flask.html",'wb')
        nuevo_archivo.write(cont_archivo)
        nuevo_archivo.close()
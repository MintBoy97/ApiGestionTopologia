from ssh_connect import conectar

def crear_Usuario(usuario, password, privilegios, ipRouter, usuario = 'admin', contra = 'admin01', secret = '1234'):
    cisco={
        "device_type":"cisco_xe",
        "ip":ipRouter,
        "username":user,
        "password":contra,
        "secret":secret
    }
    cmd = [f'username {username} privilege {privilegios} password {password}']
    conectar(cisco, cmd)
    print(f'Creado el usario: {usario} con exito')

def modificar_Usuario(usuario, password, privilegios, ipRouter, usuario = 'admin', contra = 'admin01', secret = '1234'):
    cisco={
        "device_type":"cisco_xe",
        "ip":ipRouter,
        "username":user,
        "password":contra,
        "secret":secret
    }
    cmd = [f'username {username} privilege {privilegios} password {password}']
    conectar(cisco, cmd)
    print(f'El usario: {usario} se modificó con exito')

def eliminar_Usuario(usuario, ipRouter, usuario = 'admin', contra = 'admin01', secret = '1234'):
    cisco{
        "device_type":"cisco_xe",
        "ip":ipRouter,
        "username":user,
        "password":contra,
        "secret":secret
    }
    cmd = [f'no username {usuario}']
    conectar(cisco, cmd)
    print(f'Usuario borrado con exito')

def config_RIP(network, ipRouter, usuario = 'admin', contra = 'admin01', secret = '1234'):
    cisco={
        "device_type":"cisco_xe",
        "ip":ipRouter,
        "username":user,
        "password":contra,
        "secret":secret
    }
    cmd = ['conf t', 'router rip', f'network {network}']
    conectar(cisco, cmd)
    print(f'Configuracion RIP en el router {ipRouter} se completo con exito')

def config_Estatico(ipRouter, lanConexion, NetMask, primerSalto, usuario = 'admin', contra = 'admin01', secret = '1234'):
    cisco={
        "device_type":"cisco_xe",
        "ip":ipRouter,
        "username":user,
        "password":contra,
        "secret":secret
    }
    cmd = ['conf t', f'ip route {lanConexion} {NetMask} {primerSalto}']
    conectar(cisco, cmd)

def config_OSPF():
    pass
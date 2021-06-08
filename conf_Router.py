from ssh_connect import conectar

def crear_Usuario(usuario, password, privilegios, ipRouter, usuar = 'admin', contra = 'admin01', secret = '1234'):
    cisco={
        "device_type":"cisco_xe",
        "ip":ipRouter,
        "username":usuario,
        "password":contra,
        "secret":secret
    }
    cmd = [f'username {usuario} privilege {privilegios} password {password}']
    conectar(cisco, cmd)
    print(f'Creado el usario: {usario} con exito')

def modificar_Usuario(usuario, password, privilegios, ipRouter, usuar = 'admin', contra = 'admin01', secret = '1234'):
    cisco={
        "device_type":"cisco_xe",
        "ip":ipRouter,
        "username":usuario,
        "password":contra,
        "secret":secret
    }
    cmd = [f'username {usuario} privilege {privilegios} password {password}']
    conectar(cisco, cmd)
    print(f'El usario: {usuario} se modificó con exito')

def eliminar_Usuario(usuario, ipRouter, usuar = 'admin', contra = 'admin01', secret = '1234'):
    cisco={
        "device_type":"cisco_xe",
        "ip":ipRouter,
        "username":usuario,
        "password":contra,
        "secret":secret
    }
    cmd = [f'no username {usuario}']
    conectar(cisco, cmd)
    print(f'Usuario borrado con exito')

def cambiar_Nombre_Host(usuario, ipRouter, hostname, usuar = 'admin', contra = 'admin01', secret = '1234' ):
    cisco={
            "device_type":"cisco_xe",
            "ip":ipRouter,
            "username":usuario,
            "password":contra,
            "secret":secret
        }
    cmd = [f'hostname {hostname}']
    conectar(cisco, cmd)
    print(f'El hostname se actualizo con exito a {hostname}')
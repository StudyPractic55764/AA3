import socket
import psutil
import subprocess
import re

def elegir_adaptador():

    #Listamos con un submenu todos los adaptadores disponibles
    
    incremental = 1

    adaptadores = []
    direccion_adaptador = psutil.net_if_addrs()

    for intf, addr_list in direccion_adaptador.items():
        print(f"{incremental}- {intf}")
        incremental+=1
        adaptadores.append(intf)

    #Ejecutamos un bucle hasta que el usuario eliga una opción correcta dentro la lista de adaptadores
    while True:
        try:
            eleccion=int(input(f"Elige un numero de adaptador entre 1-{len(adaptadores)}: "))

            if 1 <= eleccion <= len(adaptadores):
                adaptador_elegido = adaptadores[eleccion - 1]
                print(adaptador_elegido)
                return adaptador_elegido
            else: 
                input(f"Valor inválida, introduzca una numero entre 1-{len(adaptadores)}:")

        except ValueError:
            print("Entrada invalida. Por favor, introduzca un numero entero.")

    #Ejecutamos y capturamos la salida de ipconfig /all

    salida = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True, encoding='cp850')
    output = salida.stdout

    dns_servers = re.findall(r'Servidores DNS.*?:\s+([\d\.]+)', output)

    if dns_servers in adaptador_elegido:
        print("Servidores DNS encontrados:")
        for dns in dns_servers:
            print(f"- {dns}")
    else:
        print("No se encontraron servidores DNS.")
        
        
        
    """
    salida = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True, encoding='cp850')
    output = salida.stdout

    dns_servers = re.findall(r'Servidores DNS.*?:\s+([\d\.]+)', output)

    if dns_servers:
        print("Servidores DNS encontrados:")
        for dns in dns_servers:
            print(f"- {dns}")
    else:
        print("No se encontraron servidores DNS.")


    direccion_adaptador = psutil.net_if_addrs()
    incremental = 1

    for intf, snicaddrs in direccion_adaptador.items():
            print(f"{incremental}: {intf}\n\n")
            for snicaddr in snicaddrs:
                if snicaddr.family == psutil.AF_LINK:
                    print(f" MAC: {snicaddr.address}")
            incremental+=1
    """

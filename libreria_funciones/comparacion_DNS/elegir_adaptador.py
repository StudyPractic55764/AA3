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
                break
            else: 
                print(f"Valor inválida, introduzca una numero entre 1-{len(adaptadores)}:")

        except ValueError:
            print("Entrada invalida. Por favor, introduzca un numero entero.")

    #Ejecutamos y capturamos la salida de 'ipconfig /all'

    salida = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True, encoding='cp850')
    output = salida.stdout

    #Buscamos el adaptador que hemos elegido para que nos muestre su DNS creando un patron y seccion para separar del resto de adaptadores
    
    patron = rf'Adaptador de .*{adaptador_elegido}.*?(?=\n\s*\n|\n\w|$)'
    seccion_adaptador = re.search(patron, output, re.DOTALL | re.IGNORECASE)
    
    #Creamos una lista para almacenar si existen multiples DNS dentro el adaptador
    dns_servers = []

    if seccion_adaptador:
        texto_seccion = seccion_adaptador.group(0)

        #Buscamos el DNS en la seccion del adaptador y especificamos el patron de texto que tiene que ecncontrar
        patron_dns = r'(?:Servidores DNS|DNS Servers).*?:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        dns_servers = re.findall(patron_dns, texto_seccion, re.IGNORECASE)

        #Buscamos en lineas adicionales en caso de que existan más de una DNS
        if not dns_servers:
            todas_ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', texto_seccion)
            dns_servers = todas_ips

    #Mostramos los resultados de la DNS encontrada
    if dns_servers:
        print(f"Servidores DNS del adaptador {adaptador_elegido}:")
        for dns in set(dns_servers):
            print(f"- {dns}")
        return adaptador_elegido, list(set(dns_servers))
    else:
        print(f"No se han encontrado servidores DNS en el adaptador {adaptador_elegido}")
        return adaptador_elegido, []
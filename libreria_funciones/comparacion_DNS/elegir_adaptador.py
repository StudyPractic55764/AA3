import psutil
import subprocess
import re

def elegir_adaptador():

    print("-"*40)
    print("LISTA DE ADAPTADORES DE RED DISPONIBLES")
    print("-"*40)

    #Listamos con un submenu todos los adaptadores activos
    
    adaptadores_disponibles = []
    stats = psutil.net_if_stats()
    incremental = 1

    for nombre, stat in stats.items():
        if stat.isup:
            print(f"{incremental}- {nombre}")
            incremental+=1
            adaptadores_disponibles.append(nombre)
    if not adaptadores_disponibles:
        print("No se han encontrado adaptadores disponibles")
        return None

    #Ejecutamos un bucle hasta que el usuario eliga una opción correcta dentro la lista de adaptadores
    while True:
        try:
            eleccion=int(input(f"Elige un numero de adaptador entre 1-{len(adaptadores_disponibles)}: "))

            if 1 <= eleccion <= len(adaptadores_disponibles):
                adaptador_elegido = adaptadores_disponibles[eleccion - 1]
                print(adaptador_elegido)
                break
            else: 
                print(f"Valor inválida, introduzca una numero entre 1-{len(adaptadores_disponibles)}:")

        except ValueError:
            print("Entrada invalida. Por favor, introduzca un numero entero.")

    #Ejecutamos y capturamos la salida de 'ipconfig /all'

    salida = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True, encoding='cp850')
    output = salida.stdout

    #Buscamos el adaptador que hemos elegido para que nos muestre su DNS creando un patron y seccion para separar del resto de adaptadores
    
    patron = rf'Adaptador de .*{re.escape(adaptador_elegido)}.*?\n(.*?)(?=\n\s*Adaptador de|\n\s*\n|$)'
    seccion_adaptador = re.search(patron, output, re.DOTALL | re.IGNORECASE)
    
    #Creamos una lista para almacenar si existen multiples DNS dentro el adaptador
    dns_servers = []
    
    if seccion_adaptador:
        texto_seccion = seccion_adaptador.group(0)
        lineas = texto_seccion.splitlines()

        for i, linea in enumerate(lineas):
            if "Servidores DNS" in linea or "DNS Servers" in linea:
                ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', linea)
                dns_servers.extend(ips)

        #Buscamos el DNS en la seccion del adaptador y especificamos el patron de texto que tiene que ecncontrar
        patron_dns = r'(?i)(?:Servidores DNS|DNS Servers).*?:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        dns_servers = re.findall(patron_dns, texto_seccion, re.IGNORECASE)


        #Buscamos en lineas adicionales en caso de que existan más de una DNS
        if not dns_servers:
            todas_ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', texto_seccion)
            dns_servers = todas_ips

    #Mostramos los resultados de la DNS encontrada
    if dns_servers:
        print(f"Servidores DNS del adaptador {adaptador_elegido}:")
        for dns in dict.fromkeys(dns_servers):
            print(f"- {dns}")
        return dns_servers, adaptador_elegido
    
    else:
        print(f"No se han encontrado servidores DNS en el adaptador {adaptador_elegido}")
        return adaptador_elegido, []
    

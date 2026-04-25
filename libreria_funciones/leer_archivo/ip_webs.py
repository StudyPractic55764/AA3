import socket

def leer_ips_webs (ruta_archivo="web.txt"):

    print("-"*40)    
    print("EXTRACCION DE DIRECCIONES IP")
    print("-"*40)

    lista_IPs = []
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            
            #Saltamos lineas vacías o comentarios si existen en el archivo de texto
            if not linea or linea.startswith('#'):
                continue
            
            #Limpiamos la URL quitando http://, https://, etc
            web = linea
            if web.startswith('http://'):
                web = web[7:]
            elif web.startswith('https://'):
                web = web[8:]
            web = web.strip('/')
            if web.startswith('www.'):
                web = web[4:]
            
            
            #Extraemos la IP de la dirección web
            try:
                ip = socket.gethostbyname(web)
                print(f"{web:35} --> {ip}")
                lista_IPs.append((web, ip))
            except socket.gaierror:
                print(f"{web:35} --> ERROR: No se pudo extraer la IP")

    print("-"*40)
    return lista_IPs
    

    
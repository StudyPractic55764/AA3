#Creamos función para leer el contenido del archivo web.txt

def leer_webs_archivo(ruta_archivo = "web.txt"):
    
    print("-"*40)
    print(f"CONTENIDO DEL ARCHIVO: {ruta_archivo}")
    print("-"*40)
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(contenido)

    

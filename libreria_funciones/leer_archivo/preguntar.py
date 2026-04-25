def preguntar_ruta_archivo():
    print("-"*40)
    print("SELECCIONAR ARCHIVO DE SITIOS WEB")
    print("-"*40)

    
    ruta = input("Ingresar la ruta del archivo web.txt: ").strip()

    if ruta != "web.txt":
        ruta = "web.txt"
        print(f"Usando archivo por defecto: {ruta}")

    return ruta
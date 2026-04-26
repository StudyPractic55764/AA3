import dns.resolver
import time

def comparacion_dns_archivo(dns_server):

    print("-"*40)
    print(f"COMPARANDO VELOCIDADES DE RESPUESTA...")
    print("-"*40)

    #Creamos la lista para empezar a guardar en ella todas las direcciones DNS para esta parte del trabajo
    lista_dns = []
    for linea in dns_server:
        lista_dns.append(linea)

    #Añadiremos las direcciones DNS del archivo DNSips.txt dentro la lista creada anteriormente para luego realizar las comparaciones
    with open("DNSips.txt", 'r', encoding="utf-8") as archivo:
        for linea_dns in archivo:
            linea_dns = linea_dns.strip()
            lista_dns.append(linea_dns)
    #Mostramos la lista con todas las DNS que necesitaremos para esta parte del trabajo
    print(lista_dns)

    #Creamos una nueva lista para guardar las DNS en orden de más rapida a menos
    resultado = []


    for elemento_dns in lista_dns:
        #Creamos un resolver para hacer las consultas DNS
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [elemento_dns]
        #Especificamos el tiempo máximo de esperar para cada intento
        resolver.timeout = 2
        #Especificamos el tiempo total para realizar las consultas
        resolver.lifetime = 2

        #Creamos una lista para almacen los tiempos de cada intento en milisegundos
        tiempo_reaccion = []

        #Especificamos un numero de mediciones para realizar para obtener un promedio de ello
        for _ in range(3): 
            try: 
                inicio = time.perf_counter()
                resolver.resolve("google.com", "A")
                fin = time.perf_counter()
                tiempo_reaccion.append((fin - inicio) * 1000)
            except Exception:
                continue
        
        #Si al menos uno de los intentos a tenido exito calculamos el promedio de tiempo
        if tiempo_reaccion:
            promedio = sum(tiempo_reaccion) / len(tiempo_reaccion)

            #Guardamos los resultados finales dentro la lista
            resultado.append({"DNS": elemento_dns, "ms": promedio})
            print(f"DNS {elemento_dns:15} | Latencia media: {promedio:.2f} ms")
        else:
            print(f"DNS {elemento_dns:15} | Error: No hay respuesta")
    #Ordenamos el interior de la lista por su latencia de mayor a menor
    resultado.sort(key=lambda x: x["ms"])

    print(f"El DNS más rapida es {resultado[0]['DNS']} con un tiempo de respuesta de {resultado[0]['ms']:.2f} ms")
    return resultado
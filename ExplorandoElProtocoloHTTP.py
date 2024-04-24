import socket

try:
    # Crear un socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conectar al servidor
    mysock.connect(('data.pr4e.org', 80))
    
    # Enviar comando HTTP GET
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.sendall(cmd)
    
    # Inicializar variables para almacenar los valores de los encabezados
    last_modified = None
    etag = None
    content_length = None
    cache_control = None
    content_type = None
    
    # Recibir los datos del servidor
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        # Buscar el final de los encabezados (indicado por una línea en blanco)
        pos = data.find(b'\r\n\r\n')
        if pos != -1:
            # Si se encuentra, extraer los encabezados y los datos restantes
            headers = data[:pos].decode()
            print(headers)
            
            # Buscar y almacenar los valores de los encabezados requeridos
            lines = headers.split('\r\n')
            for line in lines:
                if line.startswith('Last-Modified:'):
                    last_modified = line.split(': ')[1]
                elif line.startswith('ETag:'):
                    etag = line.split(': ')[1]
                elif line.startswith('Content-Length:'):
                    content_length = line.split(': ')[1]
                elif line.startswith('Cache-Control:'):
                    cache_control = line.split(': ')[1]
                elif line.startswith('Content-Type:'):
                    content_type = line.split(': ')[1]
                    
            # Imprimir los valores de los encabezados requeridos
            print(f'Last-Modified: {last_modified}')
            print(f'ETag: {etag}')
            print(f'Content-Length: {content_length}')
            print(f'Cache-Control: {cache_control}')
            print(f'Content-Type: {content_type}')
            
            # Mostrar los datos restantes después de los encabezados
            print(data[pos+4:].decode(), end='')
            break
        else:
            # Si no se encuentra, mostrar todo el fragmento actual
            print(data.decode(), end='')
finally:
    # Cerrar el socket al finalizar
    mysock.close()

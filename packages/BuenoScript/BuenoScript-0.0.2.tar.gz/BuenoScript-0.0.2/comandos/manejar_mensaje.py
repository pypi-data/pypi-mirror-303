# comandos/manejar_mensaje.py

import re

def manejar_mensaje(codigo, mensaje_args):
    """
    Función para reemplazar la variable $mensaje o $mensaje[n] en el código
    con el contenido del mensaje del usuario.

    :param codigo: El código donde debe buscarse y reemplazarse $mensaje.
    :param mensaje_args: Lista de argumentos (palabras) del mensaje del usuario.
    :return: Código con el $mensaje y $mensaje[n] reemplazado.
    """
    
    # Reemplazar $mensaje[n] con el argumento en la posición n (1-indexed)
    matches = re.findall(r'\$mensaje\[(\d+)\]', codigo)  # Encuentra $mensaje[n]
    
    for match in matches:
        indice = int(match) - 1  # Convertir el índice a base 0
        if 0 <= indice < len(mensaje_args):
            # Reemplazar $mensaje[n] con el argumento correspondiente
            codigo = codigo.replace(f"$mensaje[{match}]", mensaje_args[indice])
        else:
            # Si no existe el argumento en ese índice, lo dejamos vacío
            codigo = codigo.replace(f"$mensaje[{match}]", "")

    # Reemplazar $mensaje (sin índice) con el mensaje completo
    if "$mensaje" in codigo:
        codigo = codigo.replace("$mensaje", ' '.join(mensaje_args))
    
    return codigo


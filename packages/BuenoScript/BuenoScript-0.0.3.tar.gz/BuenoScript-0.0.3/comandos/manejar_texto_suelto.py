import re

def manejar_texto_suelto(codigo):
    """
    Extrae todo el texto que no esté envuelto en ninguna función (por ejemplo, $descripcion[], $si[], etc.)
    y lo devuelve para enviarlo como texto suelto.
    
    :param codigo: El código que contiene funciones y texto suelto.
    :return: El texto suelto sin modificaciones.
    """
    # Expresión regular que encuentra funciones con formato $funcion[]
    pattern = r'\$[a-zA-Z_]+\[.*?\]'
    
    # Remover todas las funciones dejando solo el texto suelto
    texto_suelto = re.sub(pattern, '', codigo).strip()
    
    return texto_suelto if texto_suelto else None


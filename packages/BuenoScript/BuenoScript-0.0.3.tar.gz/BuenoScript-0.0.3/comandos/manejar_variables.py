
import re
# Diccionario global para almacenar variables temporales
variables_temporales = {}

def manejar_let(codigo):
    """
    Procesa el código para definir variables temporales con $let[nombre;valor].
    
    :param codigo: El código donde debe buscarse $let.
    :return: Código después de definir las variables temporales.
    """
    # Buscar y procesar $let[nombre;valor]
    pattern = r'\$let\[(.+?);(.+?)\]'
    
    def reemplazar_let(match):
        nombre_var = match.group(1).strip()
        valor_var = match.group(2).strip()
        # Guardar la variable temporal
        variables_temporales[nombre_var] = valor_var
        # Retornar una cadena vacía ya que $let no debe aparecer en el mensaje final
        return ''
    
    # Reemplazar todas las instancias de $let en el código
    return re.sub(pattern, reemplazar_let, codigo)

def manejar_get(codigo):
    """
    Procesa el código para reemplazar $get[nombre] por el valor de la variable temporal.
    
    :param codigo: El código donde debe buscarse $get.
    :return: Código después de reemplazar las variables temporales.
    """
    # Buscar y procesar $get[nombre]
    pattern = r'\$get\[(.+?)\]'
    
    def reemplazar_get(match):
        nombre_var = match.group(1).strip()
        # Retornar el valor de la variable si existe, o el nombre original si no se encuentra
        return variables_temporales.get(nombre_var, f"$get[{nombre_var}]")
    
    # Reemplazar todas las instancias de $get en el código
    return re.sub(pattern, reemplazar_get, codigo)

def limpiar_variables_temporales():
    """
    Limpia todas las variables temporales definidas con $let.
    """
    global variables_temporales
    variables_temporales.clear()


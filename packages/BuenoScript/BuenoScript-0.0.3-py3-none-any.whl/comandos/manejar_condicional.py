import re

def manejar_si(codigo):
    """
    Procesa las condiciones $si[condición;true;false] y evalúa la expresión.

    :param codigo: El código donde debe buscarse y procesarse $si.
    :return: Código con las condiciones evaluadas.
    """
    # Buscar todas las instancias de $si
    pattern = r'\$si\[(.+?);(.+?);(.+?)\]'
    
    # Mientras haya condiciones $si en el código, procesarlas
    while re.search(pattern, codigo):
        # Encontrar la primera coincidencia
        match = re.search(pattern, codigo)
        if match:
            condicion, valor_true, valor_false = match.groups()

            # Evaluar la condición
            resultado = evaluar_condicion(condicion)

            # Reemplazar $si por el valor correspondiente (true o false)
            if resultado:
                codigo = codigo.replace(match.group(0), valor_true)
            else:
                codigo = codigo.replace(match.group(0), valor_false)
    
    return codigo

def evaluar_condicion(condicion):
    """
    Evalúa una condición simple, como x == y o x > y.
    """
    pattern = r'(.+?)(==|!=|>|<|>=|<=)(.+)'
    match = re.match(pattern, condicion.strip())
    if match:
        operando1, operador, operando2 = match.groups()
        operando1 = operando1.strip()
        operando2 = operando2.strip()

        # Aquí puedes transformar a enteros o floats si es necesario
        # Evaluar la condición basada en el operador
        if operador == "==":
            return operando1 == operando2
        elif operador == "!=":
            return operando1 != operando2
        elif operador == ">":
            return float(operando1) > float(operando2)
        elif operador == "<":
            return float(operando1) < float(operando2)
        elif operador == ">=":
            return float(operando1) >= float(operando2)
        elif operador == "<=":
            return float(operando1) <= float(operando2)
    
    return False  # Asegúrate de que esta línea esté correctamente indented y termine el método.

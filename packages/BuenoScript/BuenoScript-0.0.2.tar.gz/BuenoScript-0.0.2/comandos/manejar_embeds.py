import discord
import re

def manejar_embeds(codigo):
    """
    Procesa todas las instancias de $descripcion[texto;indice],
    $titulo[texto;indice], $autor[texto;indice], $autorURL[url;indice],
    $piePag[texto;indice], $piePagIcon[url;indice], $imagen[url;indice],
    y $miniatura[url;indice] en el código y devuelve una lista de embeds
    con sus títulos, descripciones, autores, URLs, pies de página, imágenes
    y miniaturas correspondientes.
    
    :param codigo: El código donde debe buscarse y procesarse.
    :return: Una lista de embeds de Discord.
    """
    # Diccionarios para almacenar la información
    descripciones = {}
    titulos = {}
    autores = {}
    autor_urls = {}
    pie_pag = {}
    pie_pag_icon = {}
    imagenes = {}
    miniaturas = {}

    # Buscar y procesar $descripcion[texto;indice]
    pattern_descripcion = r'\$descripcion\[(.+?)(?:;(\d+))?\]'
    matches_descripcion = re.findall(pattern_descripcion, codigo)
    for match in matches_descripcion:
        texto = match[0]
        indice = int(match[1]) if match[1] else 1
        descripciones[indice] = texto

    # Buscar y procesar $titulo[texto;indice]
    pattern_titulo = r'\$titulo\[(.+?)(?:;(\d+))?\]'
    matches_titulo = re.findall(pattern_titulo, codigo)
    for match in matches_titulo:
        texto = match[0]
        indice = int(match[1]) if match[1] else 1
        titulos[indice] = texto

    # Buscar y procesar $autor[texto;indice]
    pattern_autor = r'\$autor\[(.+?)(?:;(\d+))?\]'
    matches_autor = re.findall(pattern_autor, codigo)
    for match in matches_autor:
        texto = match[0]
        indice = int(match[1]) if match[1] else 1
        autores[indice] = texto

    # Buscar y procesar $autorURL[url;indice]
    pattern_autor_url = r'\$autorURL\[(.+?);(\d+)\]'
    matches_autor_url = re.findall(pattern_autor_url, codigo)
    for match in matches_autor_url:
        url = match[0]
        indice = int(match[1])
        autor_urls[indice] = url

    # Buscar y procesar $piePag[texto;indice]
    pattern_pie_pag = r'\$piePag\[(.+?)(?:;(\d+))?\]'
    matches_pie_pag = re.findall(pattern_pie_pag, codigo)
    for match in matches_pie_pag:
        texto = match[0]
        indice = int(match[1]) if match[1] else 1
        pie_pag[indice] = texto

    # Buscar y procesar $piePagIcon[url;indice]
    pattern_pie_pag_icon = r'\$piePagIcon\[(.+?);(\d+)\]'
    matches_pie_pag_icon = re.findall(pattern_pie_pag_icon, codigo)
    for match in matches_pie_pag_icon:
        url = match[0]
        indice = int(match[1])
        pie_pag_icon[indice] = url

    # Buscar y procesar $imagen[url;indice]
    pattern_imagen = r'\$imagen\[(.+?);(\d+)\]'
    matches_imagen = re.findall(pattern_imagen, codigo)
    for match in matches_imagen:
        url = match[0]
        indice = int(match[1])
        imagenes[indice] = url

    # Buscar y procesar $miniatura[url;indice]
    pattern_miniatura = r'\$miniatura\[(.+?);(\d+)\]'
    matches_miniatura = re.findall(pattern_miniatura, codigo)
    for match in matches_miniatura:
        url = match[0]
        indice = int(match[1])
        miniaturas[indice] = url

    # Crear embeds y asignar propiedades
    embeds = []
    for indice in sorted(set(descripciones.keys()).union(
            set(titulos.keys()), 
            set(autores.keys()), 
            set(autor_urls.keys()), 
            set(pie_pag.keys()), 
            set(pie_pag_icon.keys()), 
            set(imagenes.keys()), 
            set(miniaturas.keys()))):
        
        embed = discord.Embed()
        if indice in titulos:
            embed.title = titulos[indice]
        if indice in descripciones:
            embed.description = descripciones[indice]
        if indice in autores:
            # Establecer autor y URL si existe
            if indice in autor_urls:
                embed.set_author(name=autores[indice], url=autor_urls[indice])
            else:
                embed.set_author(name=autores[indice])
        if indice in pie_pag:
            embed.set_footer(text=pie_pag[indice])  # Establecer pie de página
        if indice in imagenes:
            embed.set_image(url=imagenes[indice])  # Establecer imagen
        if indice in miniaturas:
            embed.set_thumbnail(url=miniaturas[indice])  # Establecer miniatura
        
        embeds.append(embed)

    return embeds

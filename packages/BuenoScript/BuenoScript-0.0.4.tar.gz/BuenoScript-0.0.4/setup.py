from setuptools import setup, find_packages

setup(
    name='BuenoScript',  # Nombre de tu paquete
    version='0.0.4',  # Versión del paquete
    description='BuenoScript tu alternativa de creacion bots rrapida!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Tu nombre',
    author_email='josuebuenovargas@gmail.com',
    url='https://github.com/quabwww/BuenoScript',  # URL del proyecto
    packages=find_packages(),  # Esto busca automáticamente los paquetes en tu proyecto
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versión mínima de Python
    install_requires=[
        "requests",
        "discord.py"],  # Dependencias externas
)

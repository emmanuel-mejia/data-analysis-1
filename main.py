"""

2024.04.01
    1. Vamos a crear una función para sumar dos número enteros
    Los siguientes pasos los vamos a ejecutar desde el shell interactivo de ipython
    2. Cargamos el archivo con el comando,
        %load main.py
        Una vez cargado podremos utilizar todo el contenido del archivo (clases, variables, métodos, funciones, etc)
    3. Podemos verificar la documentación de la función, con el comando,
        %pdoc suma
    4. Ejecutamos la función cargada en el shell de ipython, llamando a la función
        suma(10,30)

"""

def suma(x: int, y:int) -> int:
    """Función que nos permitirá sumar 2 números enteros 

    Args:
        x (int): Num1
        y (int): Num2

    Returns:
        int: Resultado de la suma x + y
    """

    return x + y

def price(mes1,mes2,mes3):
    """Esta funcion calcula el precio a pagar de los diferentes clientes
    Parametros:
    Mes1
    Mes2
    Mes3
    """
    precio = 0.0615
    return precio * (Mes1 + Mes2 + Mes3)


def gas2price(ListaMeses):
    """Funcion que convierte una lista de consumos de gas de diferentes clientes durante 3 meses a otra lista a precios
     a cobrar.
    Parámetros:
    Meses de 1 cliente
    Precio meses
    """

    for cliente in listaMeses:
        precio = float(input(""))
        listaMeses.append(precio)
    for precios in range(len(ListaMeses)):
    return price

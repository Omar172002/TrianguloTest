def calcular_area(base, altura):
    if base <= 0:
        raise ValueError("La base debe ser un número positivo y no cero.")
    if altura < 0:
        raise ValueError("La altura debe ser un número positivo.")
    return (base * altura) / 2
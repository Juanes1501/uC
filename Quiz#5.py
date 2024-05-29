def OLED_a_XBM(datos_OLED):
    # Inicializar la lista para las filas en formato XBM
    filas = [0] * 8
    Aux = [0] * 8
    Intermedio = [0] * 8

    for x in range(8):
        for y in range(8):
            if y == 0:
                Intermedio[y] = datos_OLED[x] % 2
                Aux[y] = datos_OLED[x] // 2
            else:
                Intermedio[y] = Aux[y - 1] % 2
                Aux[y] = Aux[y - 1] // 2

            # Asignar el bit correspondiente a la fila
            filas[y] |= Intermedio[y] << x

    return filas

def Entradas(port_ir):
    
    return input("Ingrese un número")

def Jueguito(port_ir=16,verde=15,amarillo=14,rojo=13,lista_ganadores,num_perdedor):

    ledv = machine.Pin(green, machine.Pin.OUT)
    leda = machine.Pin(yellow, machine.Pin.OUT)
    ledr = machine.Pin(red, machine.Pin.OUT)
    while True:
        ledv.off()
        ledr.off()
        leda.off()
        print('Ingrese 3 dígitos')
        try:
            c = int(Entradas(port_ir))
            d = int(Entradas(port_ir))
            u = int(Entradas(port_ir))
        except ValueError:
            print('Ups')
            continue
        numero = c*100 + d*10 + u
        
        if numero in lista_ganadores:
            ledv.on()
            return "Ganaste"
        elif numero == num_perdedor:
            ledr.on()
            return "Perdiste"
        else:
            leda.on()
            print('Presione * para continuar')
            while Entradas(port_ir) != '*':
                print('Presione * para continuar')
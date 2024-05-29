import sys
import time

import digitalio
import busio
import board

from adafruit_ov7670 import (
    OV7670,
    OV7670_SIZE_DIV16,
    OV7670_COLOR_YUV,
)

# Configuración de la cámara
cam_bus = busio.I2C(board.GP21, board.GP20)

cam = OV7670(
    cam_bus,
    data_pins=[
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
    ],
    clock=board.GP8,
    vsync=board.GP13,
    href=board.GP12,
    mclk=board.GP9,
    shutdown=board.GP15,
    reset=board.GP14,
)
cam.size = OV7670_SIZE_DIV16
cam.colorspace = OV7670_COLOR_YUV
cam.flip_y = True

print(cam.width, cam.height)

buf = bytearray(2 * cam.width * cam.height)
print('##################################')
cam.capture(buf)
print(len(list(buf)))

chars = b" .:-=+*#%@"

width = cam.width
row = bytearray(2 * width)

# Configuración del UART
uart = busio.UART(board.GP16, board.GP17, baudrate=9600)  # Ajusta los pines y la velocidad según sea necesario

while True:
    cam.capture(buf)
    for j in range(cam.height):
        for i in range(cam.width):
            row[i * 2] = row[i * 2 + 1] = 255 - buf[2 * (width * j + i)]
        #print(list(row[0:40]))
        
    mul = []

    for x in range(40):
        y = row[x] * (x + 1)
        mul.append(y)
    
    sum_mul = 0
    sum_cam = 0
    
    for n in mul:
        sum_mul += n
    #print("sum_mul", sum_mul)
    
    for m in row[0:40]:
        sum_cam += m
    #print(sum_cam)
    
    k = 5
    
    p_medio = sum_mul / sum_cam
    
    #print(p_medio)
    
    desviacion = (20 - p_medio) * k
    
    print(desviacion)
    
    # Enviar la desviación por UART
    uart.write(f"{desviacion}\n".encode('utf-8'))
    
    print()
    #time.sleep(2)

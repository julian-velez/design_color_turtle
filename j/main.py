from turtle import *       # Importa todas las funciones de turtle para dibujar
from colorsys import *     # Importa funciones para trabajar con colores (como HSV a RGB)

tracer(200)                # Acelera la animación (reduce actualizaciones de pantalla)
bgcolor('black')           # Establece el fondo en color negro
hideturtle()               # Oculta la tortuga (cursor de dibujo)
pensize(2.1)               # Define el grosor de la línea

goto(0, 240)               # Mueve la tortuga al punto (x=0, y=240)

for i in range(800):       # Bucle que se repite 800 veces para crear el patrón
    
    # Cambia el color en cada iteración usando el modelo HSV
    # i/200 hace que el color vaya cambiando gradualmente
    color(hsv_to_rgb(i / 200, 1, 1))
    
    circle(80, 90)         # Dibuja un arco de círculo (radio 80, 90 grados)
    right(180)             # Gira 180 grados hacia la derecha
    
    circle(80, 90)         # Dibuja otro arco simétrico
    left(260)              # Gira 260 grados hacia la izquierda
    
    forward(i * 0.5)       # Avanza cada vez más (crece con i)
    circle(60, 46)         # Dibuja otro arco más pequeño
    backward(i * 0.5)      # Regresa a la posición anterior

done()                     # Mantiene la ventana abierta al finalizar
import threading
import multiprocessing
import time

# Definición de la función que será ejecutada por el proceso demonio
def funcion_demonio():
    while True:
        print('Demonio ejecutándose...')
        time.sleep(2)

# Definición de la función que será ejecutada por los hilos
def tarea_hilo(num):
    print(f'Hilo {num} iniciado...')
    time.sleep(5)
    print(f'Hilo {num} completado.')


if __name__ == "__main__":
    # Creamos un proceso demonio
    proceso_demonio = multiprocessing.Process(target=funcion_demonio)
    proceso_demonio.daemon = True
    proceso_demonio.start()

    # Creamos varios hilos
    hilos = []
    for i in range(5):
        hilo = threading.Thread(target=tarea_hilo, args=(i,))
        hilos.append(hilo)
        hilo.start()

    # Esperamos a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # El proceso demonio debería finalizar cuando termina el programa principal
    print('Programa principal finalizado.')
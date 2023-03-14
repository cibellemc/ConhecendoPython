import threading
import time

def imprime_array(nome_thread, array, delay):
    for i in range(len(array)):
        print(f"{nome_thread} - {i}º elemento: {array[i]}")
        time.sleep(delay)

thread1 = threading.Thread(target=imprime_array, args=('Thread 1', ['Cibelle', 'Carlos', 'Carla'], 1))
thread2 = threading.Thread(target=imprime_array, args=('Thread 2', [1,2,3,4,5], 2))

thread1.start()
thread2.start()

# espera a finalização de ambas antes de encerrar o programa 
thread1.join()
thread2.join()
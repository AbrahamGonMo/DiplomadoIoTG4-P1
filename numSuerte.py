import random
import time

def numero():
    return random.randint(1,100)

def saludo():
    msj = "Hola este programa te devolvera tu numero de la suerte del dia de hoy!!"
    return msj

if __name__ == "__main__":
    print(saludo())
    print("Tu numero de la suerte es ...")
    time.sleep(5)
    print(numero())


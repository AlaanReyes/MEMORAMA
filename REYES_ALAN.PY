print(" ") #Espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #Datos del programador
print(" ") #Espacio

import random
import os
import platform
import time

'''
Esta lista contendra las cartas que se van a utilizar en el juego.
'''
figuritas = ["💝", "⭐", "🐻", "🍰", "🍹", "🌻"]


num_figuritas = len(figuritas)
pares = figuritas + figuritas
random.shuffle(pares)


pares_ocultos = {
    index: [figurita, False] for index, figurita in enumerate(pares, start=1)
}

def clean():
    os.system("cls" if platform.system() == "Windows" else "clear")


carta_1 = ""
carta_2 = ""
contador_fin = 0
contador_movimientos = 0


while True:
    clean()
    print("-------- 👑 ENCUENTRA LA CARTA CORRECTA 👑 ---------\n")


    for key, value in pares_ocultos.items():
        separador='\n' if key % num_figuritas == 0 else ''
        if value[1]: #-- ya encontró su pareja
            print(f"[ {value[0]} ]", end=separador)
        else:
            print(f"[ {key} ]", end=separador)

    carta_1 = input(
        "\nEscoge la primera carta (exit para salir): ").strip().lower()
    if carta_1 == "exit":
        break
    if not carta_1.isdigit() or int(carta_1) not in pares_ocultos.keys() or pares_ocultos[int(carta_1)][1]:
        continue

    carta_2 = input(
        "Escoge la segunda carta (exit para salir): ").strip().lower()
    if carta_2 == "exit":
        break
    if not carta_2.isdigit() or int(carta_2) not in pares_ocultos.keys() or pares_ocultos[int(carta_2)][1]:
        continue

    if carta_1 == carta_2:
        print(" No puedes elegir la misma carta dos veces!")
        time.sleep(2.00)
        continue

    clean()
    print("-------- 👑 ENCUENTRA LA PAREJA 👑 ---------\n")
    contador_movimientos+=1
    for key, value in pares_ocultos.items():
        separador='\n' if key % num_figuritas == 0 else ''
        if key == int(carta_1) or key == int(carta_2) or pares_ocultos[key][1]:
            print(f"[ {value[0]} ]" , end=separador)
        else:
            print(f"[ {key} ]", end=separador)

    if pares_ocultos[int(carta_1)] == pares_ocultos[int(carta_2)]:
        pares_ocultos[int(carta_1)][1] = True
        pares_ocultos[int(carta_2)][1] = True
        contador_fin+=1
        if contador_fin == num_figuritas:
            print("\n🥳 -- LO LOGRASTE -- 🥳")
            print(f"... en {contador_movimientos} movimientos\n")
            break
        else:
            print("\n😎 Felicidades, encontraste una pareja!")
        
    time.sleep(1.8)

print("------------ 👑 FIN DEL JUEGO 👑 -------------\n\n")


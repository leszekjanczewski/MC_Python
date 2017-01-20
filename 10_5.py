from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

wyniki = {}

komunikat = ""

while komunikat != "exit":
    print("Kliknij w oknie Minecrafta")
    time.sleep(10)
    mc.events.clearAll()

    mc.postToChat("Dalej!")

    time.sleep(60)

    trafienia = mc.events.pollBlockHits()
    liczbaTrafien = len(trafienia)
    mc.postToChat("Uzyles swojego miecza " + str(trafienia) + " razy.")

    nazwaGracza = input("Podaj swoja nazwe: ")
    wyniki[nazwaGracza] = liczbaTrafien

    for nazwa in wyniki:
        print(nazwa + str(wyniki[nazwa]))

    komunikat = input("Aby rozpoczac nacisnij enter w tym oknie ('exit' aby zakonczyc)")

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

wys = [100, 0]
licznik = 0

while licznik < 60:
    poz = mc.player.getTilePos()

    if poz.y < wys[0]:
        wys[0] = poz.y
    elif poz.y > wys[1]:
        wys[1] = poz.y

    licznik += 1
    time.sleep(1)

mc.postToChat("Najnizsza: " + str(wys[0]))
mc.postToChat("Najwyzsza: " + str(wys[1]))

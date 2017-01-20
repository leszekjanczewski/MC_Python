from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

bloki = []

while True:
    trafienia = mc.events.pollBlockHits()
    if len(trafienia) > 0:
        trafienie = trafienia[0]
        trafX, trafY, trafZ = trafienie.pos.x, trafienie.pos.y, trafienie.pos.z
        blok = mc.getBlock(trafX, trafY, trafZ)
        bloki.append(blok)

    if 56 in bloki:
        mc.postToChat("Udalo sie! Masz rude diamentu!")
        break

    time.sleep(0.2)

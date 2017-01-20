from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(60)

trafienia = mc.events.pollBlockHits()
blok = 103

for trafienie in trafienia:
    x, y, z = trafienie.pos.x, trafienie.pos.y, trafienie.pos.z
    mc.setBlock(x, y, z, blok)

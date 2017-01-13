from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

poz = mc.player.getPos()
x, y, z = poz.x, poz.y, poz.z

while True:
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(-0.2, 0.2)
    y = mc.getHeight(x, z)

    mc.player.setPos(x, y, z)
    time.sleep(0.1)

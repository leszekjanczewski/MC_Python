from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

poz = mc.player.getPos()
x = poz.x
y = poz.y
z = poz.z
mc.setBlock(x, y - 1, z, 103)
time.sleep(10)

poz = mc.player.getPos()
x = poz.x
y = poz.y - 1
z = poz.z
mc.setBlock(x, y, z, 103)
time.sleep(10)
poz = mc.player.getPos()
x = poz.x
y = poz.y - 1
z = poz.z
mc.setBlock(x, y, z, 103)
time.sleep(10)

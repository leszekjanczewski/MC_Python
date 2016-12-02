import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    poz = mc.player.getPos()
    mc.setBlock(poz.x, poz.y, poz.z, 38)
    time.sleep(0.2)

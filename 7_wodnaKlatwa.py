import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

licznik = 0
while licznik <= 30:
    poz = mc.player.getPos()
    mc.setBlock(poz.x, poz.y, poz.z, 8)
    time.sleep(1)

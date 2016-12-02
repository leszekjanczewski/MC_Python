import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

skok = 1
while skok <= 5:
    x = random.randint(-127, 127)
    y = random.randint(0, 64)
    z = random.randint(-127, 127)

    mc.player.setTilePos(x, y, z)
    skok += 1
    time.sleep(10)

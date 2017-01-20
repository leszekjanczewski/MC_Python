from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

poz = mc.player.getTilePos()
x, y, z = poz.x, poz.y, poz.z

bloki = [57, 41, 22, 42, 103]
blok = random.choice(bloki)

mc.setBlock(x, y, z, blok)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

poz = mc.player.getPos()
x = poz.x
y = poz.y
z = poz.z

x += random.randrange(-10, 11)
y += random.randrange(0, 11)
z += random.randrange(-10, 11)
mc.player.setPos(x, y, z)

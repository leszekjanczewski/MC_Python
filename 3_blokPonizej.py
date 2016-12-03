from mcpi.minecraft import Minecraft
mc = Minecraft.create()

poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z
typBloku = 10

y = y - 1

mc.setBlock(x, y, z, typBloku)

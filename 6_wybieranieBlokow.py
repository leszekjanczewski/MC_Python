from mcpi.minecraft import Minecraft
mc = Minecraft.create()

typBloku = int(input("Podaj typ bloku: "))
poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z

mc.setBlock(x, y, z, typBloku)

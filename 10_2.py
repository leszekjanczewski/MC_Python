from mcpi.minecraft import Minecraft
mc = Minecraft.create()

poz = mc.player.getTilePos()
x, y, z = poz.x, poz.y, poz.z

blokSchodow = 53

for stopien in range(10):
    mc.setBlock(x + stopien, y + stopien, z, blokSchodow)

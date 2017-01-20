from mcpi.minecraft import Minecraft
mc = Minecraft.create()


blok = 24  # piaskowiec
wys = 10
poziomy = reversed(range(wys))

poz = mc.player.getTilePos()
x, y, z = poz.x + wys, poz.y, poz.z

for poziom in poziomy:
    mc.setBlocks(x - poziom, y, z - poziom, x + poziom, y, z + poziom, blok)
    y += 1

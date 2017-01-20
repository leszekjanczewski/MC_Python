from mcpi.minecraft import Minecraft
mc = Minecraft.create()

poz = mc.player.getTilePos()
x, y, z = poz.x, poz.y, poz.z

gleb = 50

for glebokosc in range(gleb):
    blok = mc.getBlock(x, y - glebokosc, z)
    if blok == 56:
        mc.postToChat("Ruda diamentu znajduje sie " + str(glebokosc) + " blokow pod toba.")
        break
else:
    mc.postToChat("Pod toba nie ma blokow z ruda diamentu.")

# connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

powietrze = 0
woda = 9

while True:
    poz = mc.player.getTilePos()
    blokPonizej = mc.getBlock(poz.x, poz.y - 1, poz.z)

    if blokPonizej != powietrze and blokPonizej != woda:
        # zmień znajdujący się pod graczem blok w złoto
        mc.setBlock(poz.x, poz.y - 1, poz.z, 41)

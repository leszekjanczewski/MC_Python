from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

poz = mc.player.getTilePos()
parkietX = poz.x - 2
parkietY = poz.y - 1
parkietZ = poz.z - 2
szer = 5
dlug = 5
blok = 41
mc.setBlocks(parkietX, parkietY, parkietZ,
             parkietX + szer, parkietY, parkietZ + dlug, blok)

while parkietX <= poz.x <= parkietX + szer and parkietZ <= poz.z <= parkietZ + dlug:
    if blok == 41:
        blok = 57
    else:
        blok = 41
    mc.setBlocks(parkietX, parkietY, parkietZ,
                 parkietX + szer, parkietY, parkietZ + dlug, blok)
    # uzyskaj położenie gracza
    poz = mc.player.getTilePos()
    # poczekaj pół sekundy
    time.sleep(0.5)

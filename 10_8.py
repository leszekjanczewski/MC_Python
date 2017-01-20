from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random


def zniszczonyBlok():
    zniszczoneBloki = [48, 67, 4, 4, 4, 4]
    blok = random.choice(zniszczoneBloki)
    return blok

poz = mc.player.getTilePos()
x, y, z = poz.x, poz.y, poz.z

zniszczonaSciana = []
wys, szer = 5, 10

# Utwórz listę zniszczonych bloków
for wiersz in range(wys):
    zniszczonaSciana.append([])
    for kolumna in range(szer):
        blok = zniszczonyBlok()
        zniszczonaSciana[wiersz].append(blok)

# Ustaw bloki
for wiersz in zniszczonaSciana:
    for blok in wiersz:
        mc.setBlock(x, y, z, blok)
        x += 1
    y += 1
    x = poz.x

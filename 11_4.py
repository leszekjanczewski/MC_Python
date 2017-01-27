from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import pickle


def tworzStrukture(x, y, z, struktura):
    xStart = x
    zStart = z
    for wiersz in struktura:
        for kolumna in wiersz:
            for blok in kolumna:
                mc.setBlock(x, y, z, blok.id, blok.data)
                z += 1
            x += 1
            z = zStart
        y += 1
        x = xStart


plikPickle = open("plikPickle", "rb")
struktura = pickle.load(plikPickle)
poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z

tworzStrukture(x, y, z, struktura)

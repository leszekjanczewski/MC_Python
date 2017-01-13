from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

poz = mc.player.getTilePos()
x = poz.x + 1
y = poz.y
z = poz.z

# Dodaj 10 szklanych bloków (ID 20) do pustej listy
bloki = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
blokWpasku = 22  # Lapis lazuli

licznik = 0
while licznik <= len(bloki):
    # Dodaj setBlock() dla pozostałych bloków na liście 
    mc.setBlock(x, y, z, bloki[0])
    mc.setBlock(x, y + 1, z, bloki[1])
    mc.setBlock(x, y + 2, z, bloki[2])
    mc.setBlock(x, y + 3, z, bloki[3])
    mc.setBlock(x, y + 4, z, bloki[4])
    mc.setBlock(x, y + 5, z, bloki[5])
    mc.setBlock(x, y + 6, z, bloki[6])
    mc.setBlock(x, y + 7, z, bloki[7])
    mc.setBlock(x, y + 8, z, bloki[8])
    mc.setBlock(x, y + 9, z, bloki[9])

    licznik += 1

    # Usuń ostatni blok z listy
    del bloki[9]

    # Wstaw blok lapis lazuli na pierwszej pozycji listy
    bloki.insert(0, blokWpasku)

    time.sleep(2)

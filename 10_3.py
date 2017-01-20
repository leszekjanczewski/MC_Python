from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def ustawFilar(x, y, z, wys):
    """Tworzy filar. Argumenty określają pozycję i wysokość filaru."""
    blokSchodow = 156
    blok = 155

    # Górna część filaru
    mc.setBlocks(x - 1, y + wys, z - 1, x + 1, y + wys, z + 1, blok, 1)
    mc.setBlock(x - 1, y + wys - 1, z, blokSchodow, 12)
    mc.setBlock(x + 1, y + wys - 1, z, blokSchodow, 13)
    mc.setBlock(x, y + wys - 1, z + 1, blokSchodow, 15)
    mc.setBlock(x, y + wys - 1, z - 1, blokSchodow, 14)

    # Podstawa filaru
    mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, blok, 1)
    mc.setBlock(x - 1, y + 1, z, blokSchodow, 0)
    mc.setBlock(x + 1, y + 1, z, blokSchodow, 1)
    mc.setBlock(x, y + 1, z + 1, blokSchodow, 3)
    mc.setBlock(x, y + 1, z - 1, blokSchodow, 2)

    # Kolumna filaru
    mc.setBlocks(x, y, z, x, y + wys, z, blok, 2)

poz = mc.player.getTilePos()
x, y, z = poz.x + 2, poz.y, poz.z

for xOffset in range(0, 100, 5):
    ustawFilar(x + xOffset, y, z, 10)

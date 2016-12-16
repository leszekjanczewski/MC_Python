from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def tworzDrzewo(x, y, z):
    """Tworzy drzewo w podanych współrzędnych"""
    drewno = 17
    liscie = 18

    # pien
    mc.setBlocks(x, y, z, x, y + 5, z, drewno)

    # liscie
    mc.setBlocks(x - 2, y + 6, z - 2, x + 2, y + 6, z + 2, liscie)
    mc.setBlocks(x - 1, y + 7, z - 1, x + 1, y + 7, z + 1, liscie)

poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z


tworzDrzewo(x + 1, y, z)
tworzDrzewo(x + 3, y, z)
tworzDrzewo(x + 5, y, z)
tworzDrzewo(x + 7, y, z)
tworzDrzewo(x + 9, y, z)
tworzDrzewo(x + 11, y, z)
tworzDrzewo(x + 13, y, z)
tworzDrzewo(x + 15, y, z)
tworzDrzewo(x + 17, y, z)

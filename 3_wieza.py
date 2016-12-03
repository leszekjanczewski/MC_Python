from mcpi.minecraft import Minecraft
mc = Minecraft.create()

poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z

wys = 3
typBloku = 1

# Boki iglicy: powinny być takie jak wysokość
wysBoku = wys
mc.setBlocks(x + 1, y, z + 1, x + 3, y + wysBoku - 1, z + 3, typBloku)

# Szczyt iglicy: powinien być dwa razy większy od wysokości
wysSzczytu = wys * 3
mc.setBlocks(x + 2, y, z + 2, x + 2, y + wysSzczytu - 1, z + 2, typBloku)

# Podstawa iglicy: powinna stanowić połowę wysokości
wysPodstawy = wys / 2
mc.setBlocks(x, y, z, x + 4, y + wysPodstawy - 1, z + 4, typBloku)

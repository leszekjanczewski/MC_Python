from mcpi.minecraft import Minecraft
mc = Minecraft.create()
poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z
szer = 10
wys = 5
dlug = 6
typBloku = 4
powietrze = 0
mc.setBlocks(x, y, z, x + szer, y + wys, z + dlug, typBloku)
mc.setBlocks(x + 1, y + 1, z + 1,
             x + szer - 1, y + wys - 1, z + dlug - 1, powietrze)

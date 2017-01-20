from mcpi.minecraft import Minecraft
mc = Minecraft.create()

jednowymiarowaTeczowaLista = [0, 1, 2, 3, 4, 5]
poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z

for kolor in jednowymiarowaTeczowaLista:
    mc.setBlock(x, y, z, 35, kolor)
    y += 1

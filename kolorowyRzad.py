from mcpi.minecraft import Minecraft
mc = Minecraft.create()
dwuwymiarowaTeczowaLista = [[0, 0, 0],
                             [1, 1, 1],
                             [2, 2, 2],
                             [3, 3, 3], 
                             [4, 4, 4], 
                             [5, 5, 5]] 
poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z
Xpocz = x
for rzad in dwuwymiarowaTeczowaLista:
    for kolor in rzad:
        mc.setBlock(x, y, z, 35, kolor)
        x += 1
    y += 1
    x = Xpocz

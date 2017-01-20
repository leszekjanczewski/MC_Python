from mcpi.minecraft import Minecraft
mc = Minecraft.create()

poz = mc.player.getTilePos()
x, y, z = poz.x, poz.y, poz.z

bloki = [[35, 35, 22, 22, 22, 22, 35, 35],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 35, 35, 35, 35, 22],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 22, 22, 35, 35, 22],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [35, 35, 22, 22, 22, 22, 35, 35]]

for rzad in reversed(bloki):
    for blok in rzad:
        mc.setBlock(x, y, z, blok)
        x += 1
    y += 1
    x = poz.x

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z
kostka = [[[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]],
        [[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
        [[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
        [[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]]]
Xpocz = x
Ypocz = y

for gleb in kostka:
   for wys in reversed(gleb):
      for blok in wys:
         mc.setBlock(x, y, z, blok)
         x += 1
      y += 1
      x = Xpocz
   z += 1
   y = Ypocz

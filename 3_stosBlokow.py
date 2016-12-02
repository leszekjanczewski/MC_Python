from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 195
y = 62
z = 131
typBloku = 103
mc.setBlock(x, y, z, typBloku)

y = y + 1
mc.setBlock(x, y, z, typBloku)

y = y + 1
mc.setBlock(x, y, z, typBloku)

y = y + 1
mc.setBlock(x, y, z, typBloku)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 6
y = 5
z = 28
typBloku = 103
mc.setBlock(x, y, z, typBloku)
mc.setBlock(x, y + 1, z, typBloku)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

komunikat = input("Wpisz komunikat: ")
mc.postToChat(komunikat)

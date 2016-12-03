from mcpi.minecraft import Minecraft
mc = Minecraft.create()

nazwaUzytkownika = input("Prosze podac nazwe uzytkownika: ")
komunikat = input("Wpisz komunikat: ")
mc.postToChat(nazwaUzytkownika + ": " + komunikat)

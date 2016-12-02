from mcpi.minecraft import Minecraft
mc = Minecraft.create()

nazwaUzytkownika = input("Prosze podac nazwe uzytkownika: ")

while True:
    komunikat = input("Wpisz komunikat: ")
    if komunikat == "exit":
        break
    mc.postToChat(nazwaUzytkownika + ": " + komunikat)

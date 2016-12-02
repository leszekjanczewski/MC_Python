from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

wynik = 0
poz = mc.player.getPos()
blokPowyzej = mc.getBlock(poz.x, poz.y + 2, poz.z)

# powtórz poniższy kod, jeśli blokPowyżej to woda (8) lub stała woda (9)
while blokPowyzej == 8 or blokPowyzej == 9:
    # sekunda przerwy w wykonywaniu pętli
    time.sleep(1)
    poz = mc.player.getPos()
    blokPowyzej = mc.getBlock(poz.x, poz.y + 2, poz.z)
    wynik = wynik + 1
    # wyświetl bieżący wynik
    mc.postToChat("Biezacy wynik: " + str(wynik))
    
    
# wyswietl koncowy wynik po petli
mc.postToChat("Koncowy wynik: " + str(wynik))
# za pomocą instrukcji if sprawdź, czy wartość zmiennej wynik jest większa lub równa 6
if wynik > 6:
    # jeśli tak jest, niech nad graczem pojawią się kwiaty
    koncowaPozycja = mc.player.getTilePos()
    mc.setBlocks(koncowaPozycja.x - 5, koncowaPozycja.y + 10, koncowaPozycja.z - 5,
                 koncowaPozycja.x + 5, koncowaPozycja.y + 10, koncowaPozycja.z + 5, 38)

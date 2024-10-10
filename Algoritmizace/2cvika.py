import math
pocetKulicek =int(input("Kolik mame kulicek?"))

velkaSkupina = math.ceil(math.sqrt(pocetKulicek))
pocetVelkychSkupin = pocetKulicek // velkaSkupina
malaSkupina  = pocetKulicek - velkaSkupina * pocetVelkychSkupin

def vaz(int VelkaSkupina, int pocetVS, int malaSkupina)

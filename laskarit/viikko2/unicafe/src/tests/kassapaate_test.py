import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.koyhakortti = Maksukortti(10)

#Kateisostojen testit

    def test_luodun_kassapaatteen_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luodun_kassapaatteen_maukkaiden_maara_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_luodun_kassapaatteen_edullisten_maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaan_kateis_ostolla_rahamaara_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaan_kateis_ostolla_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(600), 200)

    def test_edullisen_kateis_ostolla_rahamaara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisen_kateis_ostolla_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(600), 360)
    
    def test_maukkaan_kateis_ostolla_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.maukkaat, 1) 

    def test_edullisen_kateis_ostolla_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(600)
        self.assertEqual(self.kassapaate.edulliset, 1) 

    def test_maukkaan_riittamattomalla_kateis_ostolla_rahamaara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisen_riittamattomalla_kateis_ostolla_rahamaara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaan_riittamattomalla_kateis_ostolla_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_edullisen_riittamattomalla_kateis_ostolla_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_maukkaan_riittamattomalla_kateis_ostolla_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_riittamattomalla_kateis_ostolla_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
###Korttiostojen testit

    def test_maukkaan_kortti_ostolla_rahamaara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_kortti_ostolla_rahamaara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_jos_kortilla_rahaa_veloitetaan_oikea_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)
    
    def test_maukas_jos_kortilla_rahaa_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_edullinen_jos_kortilla_rahaa_veloitetaan_oikea_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_edullinen_jos_kortilla_rahaa_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_maukas_jos_kortilla_rahaa_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_jos_kortilla_rahaa_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukas_jos_kortilla_ei_tarpeeksi_rahaa_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
        self.assertEqual(self.koyhakortti.saldo, 10)

    def test_edullinen_jos_kortilla_ei_tarpeeksi_rahaa_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertEqual(self.koyhakortti.saldo, 10)
    
    def test_maukas_jos_kortilla_ei_tarpeeksi_rahaa_palautetaan_false(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti), False)

    def test_edullinen_jos_kortilla_ei_tarpeeksi_rahaa_palautetaan_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti), False)
    
    def test_maukas_jos_kortilla_ei_tarpeeksi_rahaa_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_jos_kortilla_ei_tarpeeksi_rahaa_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kortille_ladattaessa_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.koyhakortti, 1000)
        self.assertEqual(self.koyhakortti.saldo, 1010)

    def test_kortille_ladattaessa_kassan_rahamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.koyhakortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
    
    def test_kortille_ladattaessa_jos_summa_negatiivinen_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.koyhakortti, -15)
        self.assertEqual(self.koyhakortti.saldo, 10)

    def test_kortille_ladattaessa_jos_summa_negatiivinen_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.koyhakortti, -15)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
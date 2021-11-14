import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.huonovarasto = Varasto(-1, -1)
        self.taysivarasto = Varasto(5, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual 
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_sallittu_tilavuus(self):
        self.assertEqual(self.huonovarasto.tilavuus, 0)

    def test_uudella_varastolla_sallittu_saldo(self):
        self.assertEqual(self.huonovarasto.saldo, 0)

    def test_uudella_varastolla_liian_iso_saldo(self):
        self.assertEqual(self.taysivarasto.saldo, 5)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_lisays_ei_toimi(self):
        self.varasto.lisaa_varastoon(6)
        self.varasto.lisaa_varastoon(-3)

        self.assertEqual(self.varasto.saldo, 6) #ei toimi

    def test_lisays_mahtuu_varastoon(self):
        self.varasto.lisaa_varastoon(100)

        self.assertEqual(self.varasto.paljonko_mahtuu(), 0) #ei toimi

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ei_voi_ottaa_negatiivista(self):
        self.assertEqual(self.varasto.ota_varastosta(-1), 0)

    def test_ei_voi_ottaa_liikaa(self):
        self.assertEqual(self.varasto.ota_varastosta(11), 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tulostus_toimii(self):
        self.varasto.lisaa_varastoon(3)
        self.assertIn(self.varasto.__str__(), "saldo = 3, vielä tilaa 7")

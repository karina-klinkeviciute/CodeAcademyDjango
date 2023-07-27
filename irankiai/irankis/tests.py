from django.contrib.auth.models import User
from django.test import TestCase

from irankis.factories import RandomUserFactory
from irankis.models import Irankis, IrankioVienetas
from naudotojo_profilis.models import NaudotojoProfilis


# Create your tests here.
class IrankiaiTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # naudotojas = User(username="test")

        # naudotoja sukuriam naudodami factory boy
        naudotojas = RandomUserFactory()
        naudotojas.save()

        # sukuriam naudotojo profili, nes pas mus irankis su naudotoju susietas per ji
        naudotojo_profilis = NaudotojoProfilis(naudotojas=naudotojas)

        # sukurus naudotojo profili, ji reikia issaugoti. Kaip ir visus modeliu objektus
        naudotojo_profilis.save()

        # sukuriam iranki, kuriam skaiciuosim laisvus irankio vienetus
        cls.irankis = Irankis(name="plaktukas", delivery=True, naudotojas=naudotojo_profilis)
        cls.irankis.save()

        # Sukuriam du iranki ovienetus. Viena ju padarom isnuomota, kita ne.
        # Taigi, laisvu vienetu skaicius turi buti 1 (nes tik vienas neisnuomotas)
        cls.irankio_vienetas1 = IrankioVienetas(irankis=cls.irankis, QR_kodas="test")
        cls.irankio_vienetas1.save()
        cls.irankio_vienetas2 = IrankioVienetas(irankis=cls.irankis, QR_kodas="Test2", ar_isnuomotas=True)
        cls.irankio_vienetas2.save()

        # atspausdinam naudotojo varda ir pavarde, factory boy veikimo patikrinimui
        print(naudotojas.first_name)
        print(naudotojas.last_name)

    def test_laisvi_irankiai_count(self):
        # testuojam, kiek yra laisvu (neisnuomotu) irankiu.
        # kvieciam modelio irankis funkcija (tiksliau, property),
        # kuri grazina neisnuomotu irankiu kieki
        laisvi = self.irankis.laisvi_irankiai_count

        # kadangi sukurem viena isnuomota ir viena neisnuomota, laisvas yra 1
        self.assertEqual(laisvi, 1)

        # pakeiciam laisva i isnuomota, ir laisvu jau 0
        self.irankio_vienetas1.ar_isnuomotas = True
        self.irankio_vienetas1.save()
        laisvi = laisvi = self.irankis.laisvi_irankiai_count

        self.assertEqual(laisvi, 0)

        # pakeiciam abu i laisvus, ir laisvu dabar 2
        self.irankio_vienetas1.ar_isnuomotas = False
        self.irankio_vienetas1.save()
        self.irankio_vienetas2.ar_isnuomotas = False
        self.irankio_vienetas2.save()
        laisvi = self.irankis.laisvi_irankiai_count

        self.assertEqual(laisvi, 2)

    def test_irankio_vienetai(self):
        vienetai = self.irankis.irankiovienetas_set.count()
        self.assertEqual(vienetai, 2)

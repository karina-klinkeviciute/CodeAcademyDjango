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
        naudotojas = RandomUserFactory()
        naudotojas.save()
        naudotojo_profilis = NaudotojoProfilis(naudotojas=naudotojas)
        naudotojo_profilis.save()
        cls.irankis = Irankis(name="plaktukas", delivery=True, naudotojas=naudotojo_profilis)
        cls.irankis.save()
        cls.irankio_vienetas1 = IrankioVienetas(irankis=cls.irankis, QR_kodas="test")
        cls.irankio_vienetas1.save()
        cls.irankio_vienetas2 = IrankioVienetas(irankis=cls.irankis, QR_kodas="Test2", ar_isnuomotas=True)
        cls.irankio_vienetas2.save()
        print(naudotojas.first_name)
        print(naudotojas.last_name)

    def test_laisvi_irankiai_count(self):

        laisvi = self.irankis.laisvi_irankiai_count
        self.assertEqual(laisvi, 1)

    def test_irankio_vienetai(self):
        vienetai = self.irankis.irankiovienetas_set.count()
        self.assertEqual(vienetai, 2)

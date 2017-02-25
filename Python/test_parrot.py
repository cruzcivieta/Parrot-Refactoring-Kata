from unittest import TestCase
from parrot import Parrot


class ParrotTest(TestCase):

    def test_speed_of_european_parrot(self):
        parrot = Parrot.european_parrot()
        self.assertEqual(12.0, parrot.speed())

    def test_speed_of_african_parrot_with_one_coconut(self):
        parrot = Parrot.african_parrot(1)
        self.assertEqual(3.0, parrot.speed())

    def test_speed_of_african_parrot_with_two_coconuts(self):
        parrot = Parrot.african_parrot(2)
        self.assertEqual(0.0, parrot.speed())

    def test_speed_of_african_parrot_with_no_coconuts(self):
        parrot = Parrot.african_parrot(0)
        self.assertEqual(12.0, parrot.speed())

    def test_speed_parrot_nailed(self):
        parrot = Parrot.nailed_parrot()
        self.assertEqual(0.0, parrot.speed())

    def test_speed_norwegian_blue_parrot(self):
        parrot = Parrot.norwegian_blue_parrot(1.5)
        self.assertEqual(18.0, parrot.speed())

    def test_speed_norwegian_blue_parrot_high_voltage(self):
        parrot = Parrot.norwegian_blue_parrot(4.0)
        self.assertEqual(24.0, parrot.speed())


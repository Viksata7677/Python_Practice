from unittest import TestCase

from advanced_module.oop.mammal.project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Viktor', 'kon', 'trak')

    def test_mammal_correct_init(self):
        self.assertEqual("Viktor", self.mammal.name)
        self.assertEqual('kon', self.mammal.type)
        self.assertEqual('trak', self.mammal.sound)
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_mammal_making_correct_sound(self):
        expected_result = "Viktor makes trak"

        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_info_method_returning_correct_info(self):
        expected_result = 'Viktor is of type kon'

        self.assertEqual(expected_result, self.mammal.info())
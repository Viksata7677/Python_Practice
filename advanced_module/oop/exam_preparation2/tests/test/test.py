from collections import deque
from unittest import TestCase, main

from advanced_module.oop.exam_preparation2.tests.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.railway_station = RailwayStation("Sofia")

    def test_correctly_passed_init(self):
        self.assertEqual(self.railway_station.name, "Sofia")
        self.assertEqual(self.railway_station.arrival_trains, deque())
        self.assertEqual(self.railway_station.departure_trains, deque())

    def test_less_name_characters_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.railway_station.name = "So"
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

        with self.assertRaises(ValueError) as ex:
            self.railway_station.name = "Sof"
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board_appends_train_info_in_arrival_trains_deque(self):
        self.assertEqual(self.railway_station.arrival_trains, deque())

        self.railway_station.new_arrival_on_board("Viktor")
        self.assertEqual(self.railway_station.arrival_trains, deque(["Viktor"]))

    def test_train_has_arrived_other_trains(self):
        self.railway_station.new_arrival_on_board("Info")
        self.assertEqual(len(self.railway_station.arrival_trains), 1)
        self.assertEqual(len(self.railway_station.departure_trains), 0)

        train_info = "Viktor"
        result = self.railway_station.train_has_arrived(train_info)
        expected_message = f"There are other trains to arrive before {train_info}."
        self.assertEqual(result, expected_message)

    def test_train_has_left_no_departure_trains(self):
        self.railway_station.new_arrival_on_board("Info")
        self.assertEqual(len(self.railway_station.arrival_trains), 1)
        self.assertEqual(len(self.railway_station.departure_trains), 0)

        result = self.railway_station.train_has_left("Info")
        self.assertFalse(result)

    def test_train_has_left_different_info(self):
        self.railway_station.new_arrival_on_board("Info")
        self.railway_station.train_has_arrived("Info")

        self.assertEqual(len(self.railway_station.departure_trains), 1)
        self.assertEqual(len(self.railway_station.arrival_trains), 0)

        result = self.railway_station.train_has_left("Info")
        self.assertTrue(result)

        self.assertEqual(len(self.railway_station.departure_trains), 0)
        self.assertEqual(len(self.railway_station.arrival_trains), 0)

        self.assertEqual(self.railway_station.departure_trains, deque() )

if __name__ == "__main__":
    main()



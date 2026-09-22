import unittest

from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):
    def setUp(self):
        self.fine = DuckFine("member-1")

    def test_initializes_member_and_total_owed(self):
        self.assertEqual(self.fine.member_id, "member-1")
        self.assertEqual(self.fine.total_owed, 0.0)

    def test_no_fee_is_charged_within_grace_period(self):
        self.assertEqual(self.fine.charge(2), 0.0)

    def test_regular_charge_applies_daily_fee_after_grace_period(self):
        self.assertEqual(self.fine.charge(5), 1.5)

    def test_deluxe_charge_doubles_the_fee(self):
        self.assertEqual(self.fine.charge(5, deluxe=True), 3.0)

    def test_charge_is_capped_at_maximum_fee(self):
        self.assertEqual(self.fine.charge(20), 5.0)

    def test_charge_adds_fee_to_total_owed(self):
        self.fine.charge(5)
        self.fine.charge(4)

        self.assertEqual(self.fine.total_owed, 2.5)

    def test_negative_days_late_raise_value_error(self):
        with self.assertRaises(ValueError):
            self.fine.charge(-1)


if __name__ == "__main__":
    unittest.main()
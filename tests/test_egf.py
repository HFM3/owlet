import unittest
from owlet import egf


class TestValidate(unittest.TestCase):

    def test_decimal_degree_validate(self):
        self.assertEqual(egf.decimal_degree_validate("-71.055631"), -71.055631)
        self.assertEqual(egf.decimal_degree_validate("-71"), -71)
        self.assertEqual(egf.decimal_degree_validate("+71"), 71)
        self.assertEqual(egf.decimal_degree_validate("71.00"), 71.00)

        with self.assertRaises(ValueError):
            egf.decimal_degree_validate("--71.055631")

        with self.assertRaises(ValueError):
            egf.decimal_degree_validate("++71.055631")

        with self.assertRaises(ValueError):
            egf.decimal_degree_validate("-71.0556.31")

        with self.assertRaises(ValueError):
            egf.decimal_degree_validate("-71.0556A31")

        with self.assertRaises(ValueError):
            egf.decimal_degree_validate("-71.0556 31")


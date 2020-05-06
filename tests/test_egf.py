import unittest
from owlet import egf
from pathlib import Path

test_dir = Path.cwd()


def egf_file_string(file_name, valid=True):
    validity = 'valid'
    if valid is False:
        validity = 'invalid'

    file_path = Path.joinpath(test_dir, f"EGF/{validity}/" + str(file_name))
    egf_str = file_path.read_text(encoding='utf-8')
    return egf_str


class TestValidate(unittest.TestCase):

    def test_validate(self):
        # PT
        self.assertEqual(egf.validate(egf_file_string("PostOfficeSquare.egf", valid=True)), True)
        # LS
        self.assertEqual(egf.validate(egf_file_string("PostOfficeSquare_Walk.egf", valid=True)), True)
        # POLY
        self.assertEqual(egf.validate(egf_file_string("PostOfficeSquare_Boundary.egf", valid=True)), True)

        # INVALID

        # geom type
        with self.assertRaises(egf.InvalidEGF):
            egf.validate(egf_file_string("PostOfficeSquare_geom_type.egf", valid=False))

        # geom type
        with self.assertRaises(egf.InvalidEGF):
            egf.validate(egf_file_string("PostOfficeSquare_geom_type.egf", valid=False))

        # single blank line at end
        with self.assertRaises(egf.InvalidEGF):
            egf.validate(egf_file_string("PostOfficeSquare_last_line_1.egf", valid=False))
        with self.assertRaises(egf.InvalidEGF):
            egf.validate(egf_file_string("PostOfficeSquare_last_line_2.egf", valid=False))

        # min sections
        with self.assertRaises(egf.InvalidEGF):
            egf.validate(egf_file_string("PostOfficeSquare_min_sections.egf", valid=False))

        # section spacing
        with self.assertRaises(egf.InvalidEGF):
            egf.validate(egf_file_string("PostOfficeSquare_section_spacing.egf", valid=False))

        # headers
        with self.assertRaises(egf.InvalidEGF):
            egf.validate(egf_file_string("PostOfficeSquare_headers.egf", valid=False))


class TestSectionSplit(unittest.TestCase):

    def test_section_split(self):
        result = ('PT', ['Park Name', 'City', 'Pond', 'Fountain'],
                  [['Post Office Square, Boston, FALSE, TRUE', '42.356243, -71.055631, 2']])
        self.assertEqual(egf.section_split(egf_file_string("PostOfficeSquare.egf", valid=True)), result)


class TestDecimalDegreeValidate(unittest.TestCase):

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


class TestAttributesValidate(unittest.TestCase):

    def test_attributes_validate(self):
        self.assertEqual(egf.attributes_validate(['attr_1', 'attr2', 'attr_3'], ['hdr_1', 'hdr2', 'hdr_3']),
                         ['attr_1', 'attr2', 'attr_3'])

        with self.assertRaises(egf.InvalidEGF):
            egf.attributes_validate(['attr_1', 'attr2', 'attr_3'], ['hdr_1', 'hdr2'])


class TestPointToGCAComponents(unittest.TestCase):
    def test_point_to_gca_components(self):
        egf_sections = 'PT', ['Park Name', 'City', 'Pond', 'Fountain'], [
            ['Post Office Square, Boston, FALSE, TRUE', '42.356243, -71.055631, 2']]

        result = ('PT', [[-71.055631, 42.356243, 2.0]],
                  [['Park Name', 'City', 'Pond', 'Fountain'], ['Post Office Square', 'Boston', 'FALSE', 'TRUE']])
        self.assertEqual(egf.point_to_gca_components(*egf_sections), result)


class TestLineStringToGCAComponents(unittest.TestCase):
    def test_line_string_to_gca_components(self):
        egf_sections = 'LS', ['Park Name', 'Feature Description'], [
            ['Post Office Square, A walk by the fountain', '42.356716, -71.055685, 0', '42.356587, -71.055769, 0',
             '42.356566, -71.055754, 0', '42.356539, -71.055746, 0', '42.356511, -71.055757, 0',
             '42.356495, -71.055790, 0', '42.356485, -71.055830, 0', '42.356389, -71.055842, 0',
             '42.356252, -71.055796, 0', '42.356046, -71.055642, 0', '42.355876, -71.055697, 0',
             '42.355828, -71.055758, 0']]

        result = ('LS',
                  [[[-71.055685, 42.356716, 0.0],
                    [-71.055769, 42.356587, 0.0],
                    [-71.055754, 42.356566, 0.0],
                    [-71.055746, 42.356539, 0.0],
                    [-71.055757, 42.356511, 0.0],
                    [-71.05579, 42.356495, 0.0],
                    [-71.05583, 42.356485, 0.0],
                    [-71.055842, 42.356389, 0.0],
                    [-71.055796, 42.356252, 0.0],
                    [-71.055642, 42.356046, 0.0],
                    [-71.055697, 42.355876, 0.0],
                    [-71.055758, 42.355828, 0.0]]],
                  [['Park Name', 'Feature Description'],
                   ['Post Office Square', 'A walk by the fountain']])

        self.assertEqual(egf.linestring_to_gca_components(*egf_sections), result)


class TestPolygonToGCAComponents(unittest.TestCase):
    def test_polygon_to_gca_components(self):
        egf_sections = 'POLY', ['Park Name', 'Feature Description'], [
            ['Post Office Square, Boundary of Post Office Square with holes for buildings', '42.356856, -71.055757, 0',
             '42.356080, -71.054976, 0', '42.355697, -71.055636, 0', '42.356003, -71.055941, 0',
             '42.356767, -71.056220, 0', '', '42.355955, -71.055522, 0', '42.355894, -71.055458, 0',
             '42.355846, -71.055546, 0', '42.355908, -71.055615, 0', '', '42.356089, -71.055312, 0',
             '42.356005, -71.055226, 0', '42.355969, -71.055288, 0', '42.356058, -71.055373, 0']]

        result = ('POLY',
                  [[[[-71.055757, 42.356856, 0.0],
                     [-71.054976, 42.35608, 0.0],
                     [-71.055636, 42.355697, 0.0],
                     [-71.055941, 42.356003, 0.0],
                     [-71.05622, 42.356767, 0.0],
                     [-71.055757, 42.356856, 0.0]],
                    [[-71.055522, 42.355955, 0.0],
                     [-71.055458, 42.355894, 0.0],
                     [-71.055546, 42.355846, 0.0],
                     [-71.055615, 42.355908, 0.0],
                     [-71.055522, 42.355955, 0.0]],
                    [[-71.055312, 42.356089, 0.0],
                     [-71.055226, 42.356005, 0.0],
                     [-71.055288, 42.355969, 0.0],
                     [-71.055373, 42.356058, 0.0],
                     [-71.055312, 42.356089, 0.0]]]],
                  [['Park Name', 'Feature Description'],
                   ['Post Office Square',
                    'Boundary of Post Office Square with holes for buildings']])

        self.assertEqual(egf.polygon_to_gca_components(*egf_sections), result)


if __name__ == '__main__':
    unittest.main()

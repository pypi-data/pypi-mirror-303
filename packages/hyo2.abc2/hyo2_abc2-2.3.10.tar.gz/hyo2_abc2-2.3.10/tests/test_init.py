import unittest

from hyo2.abc2 import name, __version__, __license__


class TestABC(unittest.TestCase):

    def test_name(self):
        self.assertGreater(len(name), 0)

    def test_version(self):
        self.assertEqual(len(__version__.split(".")), 3)
        self.assertGreaterEqual(int(__version__.split(".")[0]), 0)

    def test_license(self):
        self.assertTrue("lgpl" in __license__.lower())


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABC))
    return s

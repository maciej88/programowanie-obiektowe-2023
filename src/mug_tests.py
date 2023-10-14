import unittest
from mug import *


class TestMug(unittest.TestCase):

    def test_default_content(self):
        mug_1 = Mug('orange', 100)
        self.assertEqual(mug_1.get_content_type(), 'NOTHING')
        self.assertEqual(mug_1.get_content_amount(), 0)

    def test_other_content(self):
        mug_2 = Mug('orange', 300)
        with self.assertRaises(RuntimeError):
            mug_2.fill('juice', 200)

    def test_pour_out_liquid(self):
        mug_3 = Mug('orange', 300)
        self.assertEqual(mug_3.fill('NOTHING', 200), None)
        self.assertEqual(mug_3.pour_out_liquid(300), ('NOTHING', 200))


if __name__ == '__main__':
    unittest.main()

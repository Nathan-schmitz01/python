import unittest
from television import *

class MyTestCase(unittest.TestCase):

    def test___init__(self):
        tv1 = Television()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_power(self):
        tv1 = Television()
        tv1.power()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
        tv1.power()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
    
    def test_mute(self):
        tv1 = Television()

        tv1.power()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 1")

        tv1.mute()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
        
        tv1.power()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
        
        tv1.mute()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
        
        tv1.power()
        tv1.mute()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 1")
        
        tv1.power()
        tv1.mute()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 1")

    def test_channel_up(self):
        tv1 = Television()
        tv1.channel_up()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")

        tv1.power()
        tv1.channel_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 1, Volume = 0")

        tv1.channel_up()
        tv1.channel_up()
        tv1.channel_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
    
    def test_channel_down(self):
        tv1 = Television()
        tv1.power()
        tv1.channel_up()
        tv1.power()
        tv1.channel_down()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 1, Volume = 0")

        tv1.power()
        tv1.channel_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")

        tv1.channel_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 3, Volume = 0")

    def test_volume_up(self):
        tv1= Television()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")

        tv1.power()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 1")

        tv1.mute()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 2")

        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 2")

    def test_volume_down(self):
        tv1 = Television()
        tv1.power()
        tv1.volume_up()
        tv1.power()
        tv1.volume_down()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 1")

        tv1.power()
        tv1.mute()
        tv1.volume_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")

        tv1.volume_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")

        tv1.volume_up()
        tv1.volume_up()
        tv1.volume_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 1")

if __name__ == '__main__':
    unittest.main()
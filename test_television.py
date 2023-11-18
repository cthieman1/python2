import unittest

import television
from television import Television

class TestTelevision(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_power(self):
        my_tv = Television()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 0, Volume = 0')
        my_tv.power()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 0')

    def test_init(self):
        my_tv = Television()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 0, Volume = 0')

    def test_mute(self):
        my_tv = Television()
        my_tv.power()
        my_tv.volume_up()
        my_tv.mute()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 0')

        my_tv.mute()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 1')

        my_tv.power()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 0, Volume = 1')

        my_tv.power()
        my_tv.mute()
        my_tv.power()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 0, Volume = 0')

    def test_channel_up(self):
        my_tv = Television()
        my_tv.power()
        my_tv.channel_up()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 1, Volume = 0')

        my_tv.power()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 1, Volume = 0')

        my_tv.channel_up()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 1, Volume = 0')

        my_tv.power()
        my_tv.channel_up()
        my_tv.channel_up()
        my_tv.channel_up()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 0')

    def test_channel_down(self):
        my_tv = Television()
        my_tv.power()
        my_tv.channel_down()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 3, Volume = 0')

        my_tv.power()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 3, Volume = 0')

        my_tv.channel_down()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 3, Volume = 0')

        my_tv.power()
        my_tv.channel_down()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 2, Volume = 0')

    def test_volume_up(self):
        my_tv = Television()
        my_tv.volume_up()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 0, Volume = 0')

        my_tv.power()
        my_tv.volume_up()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 1')

        my_tv.mute()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 0')
        my_tv.volume_up()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 2')

        my_tv.volume_up()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 2')


    def test_volume_down(self):
        my_tv = Television()
        my_tv.power()
        my_tv.volume_up()
        my_tv.volume_up()
        my_tv.power()
        my_tv.volume_down()
        self.assertEqual(str(my_tv), 'Power = False, Channel = 0, Volume = 2')

        my_tv.power()
        my_tv.volume_down()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 1')

        my_tv.mute()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 0')
        my_tv.volume_down()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 0')

        my_tv.volume_down()
        self.assertEqual(str(my_tv), 'Power = True, Channel = 0, Volume = 0')
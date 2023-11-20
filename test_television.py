import pytest
from television import *



def test___init__():
    tv1 = Television()
    assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv1 = Television()
    tv1.power()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv1.power()
    assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
    
def test_mute():
    tv1 = Television()

    tv1.power()
    tv1.volume_up()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

    tv1.mute()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
    
    tv1.power()
    assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
    
    tv1.mute()
    assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
    
    tv1.power()
    tv1.mute()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
        
    tv1.power()
    tv1.mute()
    assert tv1.__str__() == "Power = False, Channel = 0, Volume = 1"

def test_channel_up():
    tv1 = Television()
    tv1.channel_up()
    assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

    tv1.power()
    tv1.channel_up()
    assert tv1.__str__() == "Power = True, Channel = 1, Volume = 0"

    tv1.channel_up()
    tv1.channel_up()
    tv1.channel_up()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
    
def test_channel_down():
    tv1 = Television()
    tv1.power()
    tv1.channel_up()
    tv1.power()
    tv1.channel_down()
    assert tv1.__str__() == "Power = False, Channel = 1, Volume = 0"

    tv1.power()
    tv1.channel_down()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

    tv1.channel_down()
    assert tv1.__str__() == "Power = True, Channel = 3, Volume = 0"

def test_volume_up():
    tv1= Television()
    tv1.volume_up()
    assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

    tv1.power()
    tv1.volume_up()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

    tv1.mute()
    tv1.volume_up()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

    tv1.volume_up()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    tv1 = Television()
    tv1.power()
    tv1.volume_up()
    tv1.power()
    tv1.volume_down()
    assert tv1.__str__() == "Power = False, Channel = 0, Volume = 1"

    tv1.power()
    tv1.mute()
    tv1.volume_down()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

    tv1.volume_down()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

    tv1.volume_up()
    tv1.volume_up()
    tv1.volume_down()
    assert tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
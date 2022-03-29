# -*- coding: utf-8 -*
'''!
  @file  get_time.py
  @brief      Read the current time and return it to the terminal
  @details    Read time and sqw pin mode
  @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license    The MIT License (MIT)
  @author     [tangjie](jie.tang@dfrobot.com)
  @version    V1.0
  @date       2021-12-16
  @url  https://github.com/DFRobot/DFRobot_CanBusHAT
'''
from __future__ import print_function
import sys
import os
sys.path.append("../")

from DFRobot_DS1307 import *

'''
  # Module I2C communication init
  # ds1307_addr I2C communication address
  # bus I2C bus
'''
DS1307 = DFRobot_DS1307()


def setup():
  while (DS1307.begin() == False):
    print ('Please check that the device is properly connected')
    time.sleep(3)
  print("DS1307 begin successfully!!!")

  '''
    # Stop RTC timer function
    # this bit is part of the seconds byte
  '''
  DS1307.stop
  
  '''
    # Start RTC timer function
    # this bit is part of the seconds byte
  '''
  DS1307.start

  '''
    # control the operation of the SQW/OUT pin
    # mode SQW Pin output mode:
    # e_square_wave_LOW, e_square_wave_HIGH, e_square_wave_1Hz, 
    # e_square_wave_4kHz, e_square_wave_8kHz, e_square_wave_32kHz
  '''
  DS1307.set_SQW_pin_mode(DS1307.e_square_wave_1Hz)


def loop():
  '''
    # Get the current output mode of SQW/OUT pin
    # Output mode:
    # e_square_wave_LOW, e_square_wave_HIGH, e_square_wave_1Hz, 
    # e_square_wave_4kHz, e_square_wave_8kHz, e_square_wave_32kHz
  '''
  if DS1307.e_square_wave_1Hz == DS1307.get_SQW_pin_mode():
    print("SQW/OUT pin: 1Hz | ", end='')

  '''
    # Get time from rtc module
    # List of the obtained time
    # time_list[0] for e_SEC type, range: 00-59
    # time_list[1] for e_MIN type, range: 00-59
    # time_list[2] for e_HR type, range: 00-23
    # time_list[3] for e_DOW type, range: 01-07
    # time_list[4] for e_DATE type, range: 01-31
    # time_list[5] for e_MTH type, range: 01-12
    # time_list[6] for e_YR type, range: 2000-2099
  '''
  time_list = DS1307.get_time()
  print("time: %u/%u/%u-%u %u:%u:%u \n" %( time_list[6], time_list[5],
  time_list[4], time_list[3], time_list[2], time_list[1], time_list[0] ))

  time.sleep(1)


if __name__ == "__main__":
  setup()
  while True:
    loop()

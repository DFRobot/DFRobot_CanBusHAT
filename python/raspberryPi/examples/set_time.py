# -*- coding: utf-8 -*
'''!
  @file  set_time.py
  @brief      Set time and start the timer, set sqw pin output
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
  # Change the following array, set all the time
  # time_list[0] e_SEC type, range 00-59
  # time_list[1] e_MIN type, range 00-59
  # time_list[2] e_HR type, range 00-23
  # time_list[3] e_DOW type, range 01-07
  # time_list[4] e_DATE type, range 01-31
  # time_list[5] e_MTH type, range 01-12
  # time_list[6] e_YR type, range 2000-2099
  #Note: an error may occur when the set value is out of range.
'''
time_list = [0, 56, 17, 2, 8, 2, 2022]


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


  DS1307.set_time(time_list)

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



if __name__ == "__main__":
  setup()

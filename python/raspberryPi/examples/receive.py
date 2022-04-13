# -*- coding: utf-8 -*
'''!
  @file  receive.py
  @brief This demo can get CanBus data. Run the demo and CanBus data can be received.
  @copyright   Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      [tangjie](jie.tang@dfrobot.com)
  @version     V1.0
  @date        2021-12-16
  @url         https://github.com/DFRobot/
'''

import can
import time  
  
can1 = can.interface.Bus(channel = 'can0',bustype = 'socketcan')

msg = can1.recv(10.0)
print(msg)

if msg is None:
   print('Timeout occurred,no message')

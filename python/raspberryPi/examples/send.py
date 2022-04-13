# -*- coding: utf-8 -*
'''!
  @file  send.py
  @brief This is a demo for CanBus sending. Run the demo and the device will send data via CanBus.
  @copyright   Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      [tangjie](jie.tang@dfrobot.com)
  @version     V1.0
  @date        2021-12-16
  @url         https://github.com/DFRobot/
'''

import time
import can

can0 = can.interface.Bus(channel = 'can1', bustype = 'socketcan')

msg = can.Message(arbitration_id=0x22, data=[0,1,2,3,4,5,6,7], is_extended_id=True)

can0.send(msg)

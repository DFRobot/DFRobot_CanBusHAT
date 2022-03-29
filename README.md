# DFRobot_CanBusHAT
* [中文版](./README_CN.md)

This CanBus expansion board features an integrated two-wire CAN and onboard DS1307 serial real-time clock(RTC), 
which is a low-power binary coded decimal (BCD) clock/calendar. <br/>
Address and data are transferred serially via a 2-wire, bidirectional bus. The clock/calendar provides seconds, minutes, hours, day, date, month, and year information. The date at the end of the month is automatically adjusted for months with fewer than 31 days, including corrections for leap year. The clock operates in either the 24-hour or 12-hour format with AM/PM indicator.  <br/>
The DS1307 has a built-in power-sense circuit that detects power failures and automatically switches to the backup supply. Timekeeping operation continues while the part operates from the backup supply.


![产品实物图](./resources/images/DFR0826.png)


## Product Link (https://www.dfrobot.com)
    SKU: DFR0826


## Table of Contents
  - [Summary](#summary)
  - [Installation](#installation)
  - [Methods](#methods)
  - [Compatibility](#compatibility)
  - [History](#history)
  - [Credits](#credits)


## Summary
* Two CAN interfaces  
* Real-Time Clock (RTC) Counts Seconds, Minutes, Hours, Date of the Month, Month, Day of the week, and Year with Leap-Year Compensation Valid Up to 2100
* I2C Serial Interface
* Programmable Square-Wave Output Signal
* Automatic Power-Fail Detect and Switch Circuitry
* Consumes Less than 500nA in Battery-Backup Mode with Oscillator Running
* Optional Industrial Temperature Range:-40°C to +85°C 


## Installation

To use the library, first download the library file, paste it into the directory you specified, then open the Examples folder and run the demo in that folder.


## Methods

```python

  def begin(self):
    '''!
      @brief Init function
      @return  Return init status
      @retval True for init success
      @retval False for init failure
    '''
  
  def get_time(self):
    '''!
      @brief Get time from rtc module
      @return List of the obtained time
      @n rtc[0] for e_SEC type, range: 00-59
      @n rtc[1] for e_MIN type, range: 00-59
      @n rtc[2] for e_HR type, range: 00-23
      @n rtc[3] for e_DOW type, range: 01-07
      @n rtc[4] for e_DATE type, range: 01-31
      @n rtc[5] for e_MTH type, range: 01-12
      @n rtc[6] for e_YR type, range: 2000-2099
    '''
  
  def get_type_time(self, type):
    '''!
      @brief Get the time of single type from rtc module
      @param type The time type to be obtained:
      @n e_SEC, e_MIN, e_HR, e_DOW, e_DATE, e_MTH, e_YR
      @return According to the selected time type, return the value in the corresponding range
      @n When reading e_SEC type, range: 00-59
      @n When reading e_MIN type, range: 00-59
      @n When reading e_HR type, range: 00-23
      @n When reading e_DOW type, range: 01-07
      @n When reading e_DATE type, range: 01-31
      @n When reading e_MTH type, range: 01-12
      @n When reading e_YR type, range: 2000-2099
    '''
  
  def set_time(self, rtc):
    '''!
      @brief According to the available array, set all the time
      @param rtc The array in the following format
      @n rtc[0] for e_SEC type, range: 00-59
      @n rtc[1] for e_MIN type, range: 00-59
      @n rtc[2] for e_HR type, range: 00-23
      @n rtc[3] for e_DOW type, range: 01-07
      @n rtc[4] for e_DATE type, range: 01-31
      @n rtc[5] for e_MTH type, range: 01-12
      @n rtc[6] for e_YR type, range: 2000-2099
      @n Note: an error may occur when the set value is out of range.
    '''
  
  def set_type_time(self, type, type_time):
    '''!
      @brief According to the set time type, upload the value in corresponding range, and set time
      @param type The time type to be obtained:
      @n e_SEC, e_MIN, e_HR, e_DOW, e_DATE, e_MTH, e_YR
      @param type_time according to the selected time type, write the value in the corresponding range
      @n When reading e_SEC type, range: 00-59
      @n When reading e_MIN type, range: 00-59
      @n When reading e_HR type, range: 00-23
      @n When reading e_DOW type, range: 01-07
      @n When reading e_DATE type, range: 01-31
      @n When reading e_MTH type, range: 01-12
      @n When reading e_YR type, range: 2000-2099
    '''
  
  def start(self):
    '''!
      @brief Start RTC timer function
      @n this bit is part of the seconds byte
    '''
  
  def stop(self):
    '''!
      @brief Stop RTC timer function
      @n this bit is part of the seconds byte
    '''

  def set_SQW_pin_mode(self, mode):
    '''!
      @brief control the operation of the SQW/OUT pin
      @param mode SQW Pin output mode:
      @n e_square_wave_LOW, e_square_wave_HIGH, e_square_wave_1Hz, 
      @n e_square_wave_4kHz, e_square_wave_8kHz, e_square_wave_32kHz
    '''
  
  def get_SQW_pin_mode(self):
    '''!
      @brief Get the current output mode of SQW/OUT pin
      @return Output mode:
      @n e_square_wave_LOW, e_square_wave_HIGH, e_square_wave_1Hz, 
      @n e_square_wave_4kHz, e_square_wave_8kHz, e_square_wave_32kHz
    '''

```


## Compatibility

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |           |            |    √     |         |
| RaspberryPi4 |     √     |            |          |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |


## History

- 2021/12/02 - Version 1.0.0 released.


## Credits

Written by tangjie(jie.tang@dfrobot.com), 2022. (Welcome to our [website](https://www.dfrobot.com/))


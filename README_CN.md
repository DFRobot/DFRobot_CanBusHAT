# DFRobot_CanBusHAT
* [English Version](./README.md)


这是一个CanBus的扩展板，集成两路can和板载DS1307串行实时时钟(RTC)是一个低功耗、
全二进制编码的十进制(BCD)时钟/日历。
地址和数据通过I2C双向总线串行传输。
时钟/日历提供秒、分钟、小时、日期、日期、月和年份的信息。
月底日期会自动按不足31天的月份进行调整，包括对闰年的调整。
该时钟以24小时或12小时的格式运行，并带有AM/PM指示器。
DS1307有一个内置的电源感应电路，可以检测电源故障并自动切换到备用电源。
当部件从备份供应运行时，继续计时操作。

![产品实物图](./resources/images/DFR0826.png)


## 产品链接 (https://www.dfrobot.com.cn)
    SKU: DFR0826


## 目录

* [概述](#概述)
* [库安装](#库安装)
* [方法](#方法)
* [兼容性](#兼容性)
* [历史](#历史)
* [创作者](#创作者)


## 概述

* 两路can接口
* 实时时钟(RTC)计数秒数，分钟，小时，月的日期，月，星期，年与闰年的补偿有效至2100年
* I2C串行接口
* 可编程方波输出信号
* 自动断电检测和开关电路
* 电池备份时消耗小于500nA振荡器运行模式
* 可选工业温度范围:-40°C + 85°C


## 库安装

要使用库, 首先下载库文件, 将其粘贴到指定的目录中, 然后打开examples文件夹并在该文件夹中运行演示。


## 方法

```python
  def begin(self):
    '''!
      @brief 初始化函数
      @return  返回初始化状态
      @retval True 表示初始化成功
      @retval False 表示初始化成失败
    '''
  
  def get_time(self):
    '''!
      @brief 从rtc模块获取时间
      @return 获取的时间的列表
      @n rtc[0]为 e_SEC 类型, 范围为: 00-59
      @n rtc[1]为 e_MIN 类型, 范围为: 00-59
      @n rtc[2]为 e_HR 类型, 范围为: 00-23
      @n rtc[3]为 e_DOW 类型, 范围为: 01-07
      @n rtc[4]为 e_DATE 类型, 范围为: 01-31
      @n rtc[5]为 e_MTH 类型, 范围为: 01-12
      @n rtc[6]为 e_YR 类型, 范围为: 2000-2099
    '''
  
  def get_type_time(self, type):
    '''!
      @brief 从rtc模块获取单个类型的时间
      @param type 要获取的时间类型:
      @n e_SEC, e_MIN, e_HR, e_DOW, e_DATE, e_MTH, e_YR
      @return 根据选择的时间类型, 返回对应范围的数值
      @n 读取 e_SEC 类型时, 范围为: 00-59
      @n 读取 e_MIN 类型时, 范围为: 00-59
      @n 读取 e_HR 类型时, 范围为: 00-23
      @n 读取 e_DOW 类型时, 范围为: 01-07
      @n 读取 e_DATE 类型时, 范围为: 01-31
      @n 读取 e_MTH 类型时, 范围为: 01-12
      @n 读取 e_YR 类型时, 范围为: 2000-2099
    '''
  
  def set_time(self, rtc):
    '''!
      @brief 根据给的数组, 设置所有时间
      @param rtc 按如下格式编辑的数组
      @n rtc[0]为 e_SEC 类型, 范围为: 00-59
      @n rtc[1]为 e_MIN 类型, 范围为: 00-59
      @n rtc[2]为 e_HR 类型, 范围为: 00-23
      @n rtc[3]为 e_DOW 类型, 范围为: 01-07
      @n rtc[4]为 e_DATE 类型, 范围为: 01-31
      @n rtc[5]为 e_MTH 类型, 范围为: 01-12
      @n rtc[6]为 e_YR 类型, 范围为: 2000-2099
      @n 注意: 超出范围的将导致设置错误
    '''
  
  def set_type_time(self, type, type_time):
    '''!
      @brief 根据选择设置的时间类型, 传入对应范围的数值, 设置时间
      @param type 要获取的时间类型:
      @n e_SEC, e_MIN, e_HR, e_DOW, e_DATE, e_MTH, e_YR
      @param type_time 根据选择的时间类型, 写入对应范围的数值
      @n 读取 e_SEC 类型时, 范围为: 00-59
      @n 读取 e_MIN 类型时, 范围为: 00-59
      @n 读取 e_HR 类型时, 范围为: 00-23
      @n 读取 e_DOW 类型时, 范围为: 01-07
      @n 读取 e_DATE 类型时, 范围为: 01-31
      @n 读取 e_MTH 类型时, 范围为: 01-12
      @n 读取 e_YR 类型时, 范围为: 2000-2099
    '''
  
  def start(self):
    '''!
      @brief 启动RTC计时功能
      @n this bit is part of the seconds byte
    '''
  
  def stop(self):
    '''!
      @brief 停止RTC计时功能
      @n this bit is part of the seconds byte
    '''
  
  def set_SQW_pin_mode(self, mode):
    '''!
      @brief control the operation of the SQW/OUT pin
      @param mode SQW Pin 输出模式:
      @n e_square_wave_LOW, e_square_wave_HIGH, e_square_wave_1Hz, 
      @n e_square_wave_4kHz, e_square_wave_8kHz, e_square_wave_32kHz
    '''
  
  def get_SQW_pin_mode(self):
    '''!
      @brief 获取 SQW/OUT pin 当前输出模式
      @return 输出模式:
      @n e_square_wave_LOW, e_square_wave_HIGH, e_square_wave_1Hz, 
      @n e_square_wave_4kHz, e_square_wave_8kHz, e_square_wave_32kHz
    '''

```


## 兼容性

* RaspberryPi 版本

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |           |            |    √     |         |
| RaspberryPi4 |     √     |            |          |         |

* Python 版本

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |


## 历史

- 2021/12/03 - 1.0.0 版本


## 创作者

Written by tangjie(jie.tang@dfrobot.com), 2022. (Welcome to our [website](https://www.dfrobot.com/))


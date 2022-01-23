

#导入相关模块
import network,usocket,time
from machine import I2C,Pin,Timer
from ssd1306 import SSD1306_I2C
import ure
import sys
import time


def draw_chinese(lcd,ch_str,x_axis,y_axis):
  offset_=0
  y_axis=y_axis*16#中文高度一行占8个
  x_axis=(x_axis*16)#中文宽度占16个
  for k in ch_str:
      byte_data=byte2[k]
      for y in range(0,16):
          a_=bin(byte_data[y]).replace('0b','')
          while len(a_)<8:
              a_='0'+a_
          b_=bin(byte_data[y+16]).replace('0b','')
          while len(b_)<8:
              b_='0'+b_
          for x in range(0,8):
              lcd.pixel(x_axis+x-offset_,y+y_axis,int(a_[x]))#文字的上半部分
              lcd.pixel(x_axis+x+8-offset_,y+y_axis,int(b_[x]))#文字的下半部分
      offset_+=16
      
      
      
byte2={
  "我":
    [0x04,0x0E,0x78,0x08,0x08,0xFF,0x08,0x08,0x0A,0x0C,0x18,0x68,0x08,0x08,0x2B,0x10,
    0x40,0x50,0x48,0x48,0x40,0xFE,0x40,0x44,0x44,0x48,0x30,0x22,0x52,0x8A,0x06,0x02],#我
  "x":
[0x00,0x00,0x60,0x20,0x10,0x08,0x04,0x03,0x03,0x07,0x0C,0x18,0x10,0x30,0x00,0x00,
0x00,0x02,0x0E,0x18,0x30,0x60,0x80,0x00,0x00,0x80,0xC0,0x60,0x30,0x1C,0x04,0x02],

}


#初始化相关模块
i2c = I2C(sda=Pin(13), scl=Pin(14),freq=800000)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)
oled.fill(0)
draw_chinese(oled,'我',0,3)
draw_chinese(oled,'x',1,3)
oled.show()

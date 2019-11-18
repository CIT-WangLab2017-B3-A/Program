#!/usr/bin/python
#coding: utf-8
import os
import wiringpi as wp
import time

# SPI channle (0 or 1)
MCP_CH = 0
# pin base (above 64)
PIN_BASE=70

# registance
#R1=4.10*1000.0  # [Ω]
#R2=5.32*1000.0  # [Ω]
R1=3.9*1000.0  # [Ω]
R2=5.6*1000.0  # [Ω]

#voltage
Vcc_MAX=12.0 # [V]
Vdd=4.8 # [V]
Vref=Vdd
Vlsb=Vref/1024.0

#amplitude
#Iin= 10.0*0.000001 # [A]
Iin= 0.000644972877057 # [A]

# setup
wp.mcp3002Setup (PIN_BASE, MCP_CH)
wp.wiringPiSetupGpio()
SumRegistance = R1+R2

#sumI=0.0
#for i in xrange(100):
while True:
    mcp3002_data = float(wp.analogRead(PIN_BASE+MCP_CH))
    Vin = ((mcp3002_data/1024.0)*Vdd) # 2.988[V] if Vcc=7.4[V]
    Vcc = (Vin/R2+Iin)*SumRegistance
    if Vcc < 6.2:
        print "<ここでシャットダウン操作>"
        time.sleep(2.0)
        break
        #os.system('sudo poweroff')
    elif Vcc < 6.3: # <3.15[V/cel](絶対目安)
        print "ヤバイ(早く充電): ",
    elif Vcc < 6.6: # 3.15<3.3[V/cel](安心目安)
        print "ピンチ(そろそろ充電): ",
    else:
        print "大丈夫(使用可能): ",
    print Vcc
    time.sleep(1.0)

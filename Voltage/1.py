import wiringpi as wp
import time

# SPI channle (0 or 1)
MCP_CH = 0
# pin base (above 64)
PIN_BASE=65

# setup
wp.mcp3002Setup (PIN_BASE, MCP_CH)
#wp.wiringPiSetupGpio()

while True:
    value = float(wp.analogRead(PIN_BASE))*0.004652981427175*2.421052631579
#    value = float(wp.analogRead(PIN_BASE))*0.0048828125*2.4358974359
    print (value)
    time.sleep(1)

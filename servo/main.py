#!/usr/bin/python
# coding: utf-8

## model: Futaba RS304MD
## Temprate of move program

# import Library
from move import move
import time

# main program
def main():
    servo = move()
    servo.Stand('parameter/StandAll.csv')
    time.sleep(1.0)
    servo.ahead('Ahead0.csv',0.01)
    for i in xrange(10):
        servo.ahead('DownRight.csv',0.05)
        servo.ahead('PullRight.csv',0.075)
        servo.ahead('DownLeft.csv',0.05)
        servo.ahead('PullLeft.csv',0.075)
    servo.Stand('parameter/StandAll.csv')
#    servo.Action('Ball/BallCatch.csv',0.55)
#    servo.Stand('parameter/StandAll.csv')
#    for i in xrange(5):
#        servo.ahead('Ahead0.csv',0.1)
#        servo.ahead('DownRight.csv',0.1)
#        servo.ahead('PullRight.csv',0.1)
#        servo.ahead('DownLeft.csv',0.1)
#        servo.ahead('PullLeft.csv',0.1)
#    time.sleep(1.0)
#    servo.Action('Ball/BallDust.csv',1.0)
#    time.sleep(1.0)
#    servo.Stand('parameter/StandAll.csv')
#    servo.Action('hoge.csv',2.0)
    time.sleep(1.0)
    servo.Close()

if __name__ == '__main__':
    main()
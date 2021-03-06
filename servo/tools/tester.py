## model: Futaba RS304MD
## Temprate of move program

# import Library
import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from uart import uart

# main program
def main():    
    args = sys.argv
    argc = len(args)
    servo = uart()
    for i in xrange(argc-1):
        servo.Tester(int(args[i+1]))
    servo.Close()


if __name__ == '__main__':
    main()


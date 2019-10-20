from smbus import SMBus
import time
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
#bus.write_byte(addr, 0x1) # switch it on

def readNumber():
    number = bus.read_byte(addr)
    # number = bus.read_byte_data(address, 1)
    return number

##input("Press return to turn it off")
##bus.write_byte(addr, 0x0) # switch it off
##
##input("Press return to turn it back on")
##bus.write_byte(addr, 0x1) # switch it off
##
##input("Press return to turn it off")
##bus.write_byte(addr, 0x0) # switch it off
while True:
    
#input("Press return first num")
    bus.write_byte(addr, 0x0) # look for first number
    num0 = readNumber()
    time.sleep(.1)

##input("Press return second num")
##bus.write_byte(addr, 0x1) # look for second number
##num1 = readNumber()
##
##input("Press return third num")
##bus.write_byte(addr, 0x2) # look for third number
##num2 = readNumber()
##
##input("Press return fourth num")
##bus.write_byte(addr, 0x3) # look for fourth number
##num3 = readNumber()
##
##input("Press return fifth num")
##bus.write_byte(addr, 0x4) # look for fifth number
##num4 = readNumber()
##
##print(num0, " | ", num1, " | ", num2, " | ", num3, " | ", num4)
    print (num0);
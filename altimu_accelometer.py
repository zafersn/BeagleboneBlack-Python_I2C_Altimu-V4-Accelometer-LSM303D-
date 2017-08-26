from Adafruit_I2C import Adafruit_I2C
from time import sleep


CTRL2             = 0x21
CTRL1             = 0x20
CTRL5             = 0x24
CTRL6             = 0x25
CTRL7             = 0x26

i2c = Adafruit_I2C(0x1D)


i2c.write8(CTRL2, 0x18)
i2c.write8(CTRL1, 0x57)
i2c.write8(CTRL5, 0x64)
i2c.write8(CTRL6, 0x20)
i2c.write8(CTRL7, 0x00)



print("X axis")


for x in range(0, 100):
        # getting values from the registers
        b = i2c.readS8(0x29)
        s = i2c.readU8(0x28)
        # converting 2 8 bit words into a 16 bit
        # signed "raw" value
        raw = b * 256 + s


        print (str(raw))
        sleep(0.1)


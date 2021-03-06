# BeagleboneBlack-Python_I2C_Altimu-V4-Accelometer-LSM303D-
Beagle bone üzerinde Adafruit python I2C  kütüphanesini kullanarak Altimu -V4 Accelometer verisi okuma

# DİKKAT!!!<br>
## Bu repo tamamen test amaçlı oluşturulmuştur. Sadece beaglebon' üzerinde Adafruit' in i2c kütüphaneleri denenmek için hazırlanmıştır. Oluşturulurken L3GD20H datasheet referans alınmıştır. 
<br>

Altimu-V4 'ün BBB ile I2C  bağlantıları yapıldığında **i2cdetect -y -r 1** komutunu kullanarak I2C yoluna bağlı bulunun cihazların I2C adresleri tespit edilir.
Aşağıdaki resimde görüldüğü gibi.<br>

![Screen Shot](https://github.com/zafersn/BeagleboneBlack-Python_I2C_Altimu-V4-GYRO--L3GD20H-/blob/master/img/1.png)<br>

1d = accelerometer & magnometer<br>
6b = gyro <br>
5d = barometer<br>
<br>

# Pin şeması 
I2C Pin bağlantılarım P9_19 ve p9_20 dir
![Screen Shot](https://github.com/zafersn/BeagleboneBlack-Python_I2C_Altimu-V4-Accelometer-LSM303D-/blob/master/img/beaglebone-black-pinout.jpg)<br>

![Screen Shot](https://github.com/zafersn/BeagleboneBlack-Python_I2C_Altimu-V4-Accelometer-LSM303D-/blob/master/img/IMG_20170826_205230.jpg)<br>

# Referanslar <br>

### https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/i2c

### https://www.pololu.com/product/2470

### https://www.pololu.com/file/download/LSM303D.pdf?file_id=0J703

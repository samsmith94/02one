# 02one

## Biztonságos fájl-átvitel Windows-ról Raspberry-re:
#### SCP kliens letöltése
Le kell tölteni a `pscp.exe` fájlt [innen](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).
A letöltött .exe helyét vagy fel kell fűzni a `PATH`-ra, vagy pedig az .exe fájl könyvtárából kiadni a parancsokat.

#### Fájl átvitele
`pspc -pw yourpassword filename pi@raspberrypi:/home/pi/filename`
ahol `yourpassword` a jelszó (alapértelmezetten raspberry)

Tehát pl. test.py átvitele:
`pspc -pw raspberry test.py pi@raspberrypi:/home/pi/test.py`.

#### Könyvtár átvitele
A `-r` kapcsolót kell használni:
`pscp -pw raspberry -r folder\* pi@raspberrypi:/home/pi/`.

## Ultrahangos távolságmérő használata
A távolságmérő használatához semmilyen telepítendő függőség nem szükséges, csupán az alapértelmezetten telepített `RPi.GPIO` package.

Működő példakód: [ultrasonic_sensor.py](./test/ultrasonic_sensor.py)

## Folyadék-áramlásmérő használata
A folyadék-áramlásmérő használatához semmilyen telepítendő függőség nem szükséges, csupán az alapértelmezetten telepített `RPi.GPIO` package.

Működő példakód: [flowmeter.py](./test/flowmeter.py)

## Hőmérő használata
A hőmérő használatához engedélyezni kell a 1-wire buszt, a következőképpen:
```
sudo raspi-config
```
Aztán `Interfacing Options` -> `1-Wire` -> `Igen` -> `Ok` -> `Finish`
Végül érdemes reboot-olni:
```
sudo reboot
```
Működő példakód: [thermometer.py](./test/thermometer.py)

## LCD használata
A kijelző használata az I/O Expanderrel együtt nagyon kényelmes az [RPLCD package](https://rplcd.readthedocs.io/en/stable/) segítségével.
Telepítése:
```
sudo pip install RPLCD
```
Szükség van még a python-smbus2 telepítésére is az I2C használata miatt:
```
sudo apt install python-smbus
```
Végül érdemes lehet telepíteni az i2c-tools-t is, hogy leellenőrizhessük a buszra csatlakozó eszközök címét.
Telepítése:
```
sudo apt-get install -y i2c-tools
```
Használata:
```
sudo i2cdetect -y 1
```

A kijelző használatához engedélyezni kell a I2C buszt, a következőképpen:
```
sudo raspi-config
```
Aztán `Interfacing Options` -> `I2C` -> `Igen` -> `Ok` -> `Finish`

Működő példakód: [lcd.py](./test/lcd.py)

## Modbus használata
A soros port használatához engedélyezni kell a UART-ot, a következőképpen:
```
sudo raspi-config
```
Aztán `Interfacing Options` -> `Serial` -> `Igen` -> `Ok` -> `Finish`

Működő példakód: [modbus.py](./test/modbus.py)

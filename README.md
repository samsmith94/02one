# 02one

## Biztonságos fájl-átvitel Windows-ról Raspberry-re:
### SCP kliens letöltése
Le kell tölteni a `pscp.exe` fájlt [innen](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).
A letöltött .exe helyét vagy fel kell fűzni a `PATH`-ra, vagy pedig az .exe fájl könyvtárából kiadni a parancsokat.

### Fájl átvitele
`pspc -pw yourpassword filename pi@raspberrypi:/home/pi/filename`
ahol `yourpassword` a jelszó (alapértelmezetten raspberry)

Tehát pl. test.py átvitele:
`pspc -pw raspberry test.py pi@raspberrypi:/home/pi/test.py`.

### Könyvtár átvitele
A `-r` kapcsolót kell használni:
`pscp -pw raspberry -r folder\* pi@raspberrypi:/home/pi/`.

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

Működő példakód: [lcd.py](./test/lcd.py)

## Ultrahangos távolságmérő használata

## Folyadék-áramlásmérő használata

## Hőmérő használata
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
lcd.write_string('Hello')
lcd.cursor_pos = (1, 0)
lcd.write_string('World!')
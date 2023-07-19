##threading use
import time
import sys
import os
import threading

def dump():
    while 1:
        x=0

def animation():
    sys.stdout.write("\r /")
    sys.stdout.flush()
    time.sleep(.122)
    sys.stdout.write("\r |")
    sys.stdout.flush()
    time.sleep(.122)
    sys.stdout.write("\r ─")
    sys.stdout.flush()
    time.sleep(.122)
    sys.stdout.write("\r \\")
    sys.stdout.flush()

Test = threading.Thread(target=dump)

Test.start()

while Test.is_alive():
    animation()

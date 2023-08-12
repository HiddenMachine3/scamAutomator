import subprocess

# enter the folder where you have installed ADB on PC
adb_folder_path = "C:/ADB/platform-tools"


def take_screenshot(filename):
    cmd = f"{adb_folder_path}/adb shell screencap -p"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    binary_screenshot = process.stdout.read()
    binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
    f = open(filename, "wb")
    f.write(binary_screenshot)
    f.close()

import json
import subprocess
import time

with open('contacts.json') as json_file:
    contacts = json.load(json_file)

subprocess.run(['adb', 'shell', 'am', 'force-stop', 'com.android.contacts'])

i=0
contact = contacts[0]

i+=1
name = contact['name']
name = name.replace(" ",  "_")
number = contact['number']

subprocess.run(['adb', 'shell', 'am', 'start',
                '-a','android.intent.action.INSERT',
                '-t','vnd.android.cursor.dir/contact',
                '-e','name', name])
# time.sleep(1)
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_BACK'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent','KEYCODE_BACK'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent','KEYCODE_BACK'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent',
#                 'KEYCODE_BACK'])
# subprocess.run(['adb', 'shell', 'input', 'keyevent',
#                 'KEYCODE_BACK'])
time.sleep(1)
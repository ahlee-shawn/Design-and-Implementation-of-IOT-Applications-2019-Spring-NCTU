import time
import DAN
import pyautogui

ServerURL = 'http://140.113.199.186:9999'      #with non-secure connection
#ServerURL = 'https://DomainName' #with SSL connection
Reg_addr = '5555' #  if None, Reg_addr = MAC address

DAN.profile['dm_name']='fly_simulator_output'
DAN.profile['df_list']=['Gear', 'Calibrate', 'Terminate', 'Add_speed', 'Minus_speed', 'Current_flap', 'Sign_x',
                        'X', 'Sign_y', 'Y', 'Sign_z', 'Z']
#  DAN.profile['d_name']= 'Assign a Device Name'

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#  DAN.deregister()  #if you want to deregister this device, uncomment this line
#  exit()            #if you want to deregister this device, uncomment this line
screen_size = pyautogui.size()
height = screen_size.height
width = screen_size.width
screen_y = height / 2
screen_x = width / 2
gear = 1
current_flap = 0
sign_x = 0
sign_y = 0
sign_z = 0
xxx = 0
y = 0
z = 0
add_speed = 0
minus_speed = 0
while True:
    try:
        x = DAN.pull('Gear')
        if x is not None:
            if gear != x[0]:
                pyautogui.press('g')
            gear = x[0]
        print('a')
        x = DAN.pull('Calibrate')
        if x is not None:
            calibrate = x[0]
        print('b')
        x = DAN.pull('Terminate')
        if x is not None:
            terminate = x[0]
        print('c')
        x = DAN.pull('Add_speed')
        if x is not None:
            add_speed = x[0]
        print('d')
        x = DAN.pull('Minus_speed')
        if x is not None:
            minus_speed = x[0]
        x = DAN.pull('Current_flap')
        if x is not None:
            tmp = x[0]
            if tmp > current_flap:
                pyautogui.press('f')
                current_flap = tmp
            elif tmp < current_flap:
                pyautogui.hotkey('shift', 'f')
                current_flap = tmp
        x = DAN.pull('Sign_x')
        if x is not None:
            sign_x = x[0]
        x = DAN.pull('X')
        if x is not None:
            xxx = x[0]
        x = DAN.pull('Sign_y')
        if x is not None:
            sign_y = x[0]
        x = DAN.pull('Y')
        if x is not None:
            y = x[0]
        x = DAN.pull('Sign_z')
        if x is not None:
            sign_z = x[0]
        x = DAN.pull('Z')
        if x is not None:
            z = x[0]
        if sign_x == 0:
            move_x = int(-1 * xxx)
        else:
            move_x = int(xxx)
        if sign_y == 0:
            move_y = int(-1 * y)
        else:
            move_y = int(y)
        if sign_z == 0:
            move_z = int(-1 * z)
        else:
            move_z = int(z)

        print(move_y, move_z)
        if move_y == 0 and move_z == 0:
            screen_y = height / 2
            screen_x = width / 2
        else:
            if move_z > 0:
                screen_y -= 10
            elif move_z < 0:
                screen_y += 10
            if move_y > 0:
                screen_x -= 20
            elif move_y < 0:
                screen_x += 20
        if width / 4 > screen_x:
            screen_x = width / 4
        elif screen_x > 3*width / 4:
            screen_x = 3*width / 4
        if screen_y < height / 4:
            screen_y = height / 4
        elif screen_y > 3*height / 4:
            screen_y = 3*height / 4
        pyautogui.moveTo(screen_x, screen_y, 0.1)
        print(add_speed)
        if add_speed == 1:
            pyautogui.keyDown('pageup')
        else:
            print("keyUp")
            pyautogui.keyUp('pageup')
        if minus_speed == 1:
            pyautogui.keyDown('pagedown')
        else:
            pyautogui.keyUp('pagedown')
    except Exception as e:
        print(e)
        continue

    time.sleep(0.1)

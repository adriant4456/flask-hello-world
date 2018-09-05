#Check in gui automation
import pyautogui
import win32gui
import win32con
import time
import datetime
import shutil
import os

#todo move exploded bom to material folder NOT desktop
def mbom(material):
    pyautogui.PAUSE = 0.5
    handle = WindowEnumerate('SAP Easy Access')
    print(handle)
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(handle)
    pyautogui.moveTo(100,215)
    pyautogui.doubleClick()
    waitforwindow('Explode BOM')
    pyautogui.typewrite(str(material))
    pyautogui.hotkey('tab')
    pyautogui.typewrite('3010')
    pyautogui.hotkey('f8')
    waitforwindow('Display Multilevel BOM')
    material = str(material)
    if not os.path.isdir(f"C:\\Users\\atai\\Desktop\\{material}"):
        os.mkdir(f"C:\\Users\\atai\\Desktop\\{material}")
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'shift', 'f9')
    time.sleep(1)
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('delete')
    pyautogui.typewrite(str(material))
    pyautogui.typewrite('.XLS')    
    pyautogui.hotkey('up')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('delete')
    pyautogui.typewrite('C:\\Users\\atai\\Desktop\\')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('f12')
    pyautogui.hotkey('f12')

def plot_struc(material):
    pyautogui.PAUSE = 0.5
    handle = WindowEnumerate('SAP Easy Access')
    print(handle)
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(handle)
    pyautogui.moveTo(79,196)
    pyautogui.doubleClick()
    waitforwindow('BOM Plot')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.typewrite(str(material))
    pyautogui.hotkey('tab')
    pyautogui.typewrite('3010')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.typewrite('1')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('space')
    pyautogui.hotkey('f8')
    while True:
        modified_list = []
        out = False
        for i in os.listdir('C:\\Temp'):
            mtime = os.path.getmtime('C:\\Temp\\' + i)
            current_time = time.time()
            if (current_time - mtime) < 60: #check if file was created in last 1 mins
                modified_list.append(i)
            print(modified_list)
        for i in modified_list:
            if 'isbom' in i:
                print('should break')
                out = True
                break
        if out:
            break
        time.sleep(0.5)
    time.sleep(1)
    if not pyautogui.confirm('Continue to DocStructure?') == 'OK':
        exit()
    handle = WindowEnumerate('BOM Plot')
    print(handle)
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(handle)
    pyautogui.hotkey('f12')
    pyautogui.hotkey('f12')
    modified_list = []
    for i in os.listdir('C:\\Temp'):
        mtime = os.path.getmtime('C:\\Temp\\' + i)
        current_time = time.time()
        if (current_time - mtime) < 120: #check if file was created in last 2 mins
            if "tmp" not in i:
                modified_list.append(i)
    #find name of file
    try:
        folder_name = modified_list[1].split('.')[0]
    except:
        print('Can\'t find files')
        exit()
    folder_dir = 'C:\\Users\\atai\\Desktop\\' + folder_name
    if not os.path.isdir(f"C:\\Users\\atai\\Desktop\\{material}"):
        os.mkdir(folder_dir)
    for i in modified_list:
        shutil.move('C:\\Temp\\' + i, folder_dir)
    pyautogui.hotkey('up')
    pyautogui.hotkey('enter')
    pyautogui.typewrite(str(material))
    pyautogui.hotkey('f8')
    while True:
        modified_list = []
        out = False
        for i in os.listdir('C:\\Temp'):
            mtime = os.path.getmtime('C:\\Temp\\' + i)
            current_time = time.time()
            if (current_time - mtime) < 60: #check if file was created in last 1 mins
                modified_list.append(i)
            print(modified_list)
        for i in modified_list:
            if 'ErrorLog' in i:
                print('should break')
                out = True
                break
        if out:
            break
        time.sleep(0.5)
    time.sleep(1)
    modified_list = []
    for i in os.listdir('C:\\Temp'):
        mtime = os.path.getmtime('C:\\Temp\\' + i)
        current_time = time.time()
        if (current_time - mtime) < 120: #check if file was created in last 2 mins
            modified_list.append(i)
    for i in modified_list:
        if 'ErrorLog' in i:
            shutil.move('C:\\Temp\\' + i, folder_dir)
    time.sleep(1)
    if not pyautogui.confirm('Continue to SAP?') == 'OK':
        exit()
    handle = WindowEnumerate('INVENTOR DOCUMENT STRUCTURE')
    print(handle)
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(handle)
    pyautogui.moveTo(360,206)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    waitforwindow('Save As')
    pyautogui.typewrite(str(material) + '.MHTML')
    while True:
        out = False
        for i in os.listdir('C:\\Users\\atai\\Documents\\SAP\\SAP GUI'):
            if str(material) in i:
                out = True
                break
        if out:
            break
    shutil.move('C:\\Users\\atai\\Documents\\SAP\\SAP GUI\\' + str(material) + '.MHTML', folder_dir)
        
        
    
        

    
    
    
def waitforwindow(window):
    while True:
        if WindowEnumerate(window):
            break
    

def WindowEnumerate(window):
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if window in i[1]:
            print(i)
            return i[0]
    return False

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


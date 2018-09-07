import subprocess       #To open/close external programs
import time             #To use sleep function, program waits
import shutil           #To rename files/folders
import os               #To search for file names
import psutil           #To search for inventor pid to kill
import win32gui
import win32con


def change(folder):
    #check for folder_name.txt in source folder
    source_path = 'C:\\InventorWork'
    destination_path = 'C:\\' + folder
    if os.path.isfile(source_path + '\\' + 'folder_name.txt'):
         pass
    else:
        raise LookupError('Cannot find folder_name.txt')
    #check for folder_name in destination folder
    if os.path.isfile(destination_path + '\\' + 'folder_name.txt'):
        pass
    else:
        no_proj(None, None, folder)     #create folder_name.txt with folder as name
    iw_change = 'C:\\' + folder
    if os.path.exists(iw_change):
        if kill():
            rename()
            time.sleep(1)
            time.sleep(1)
            os.rename(iw_change, 'C:\\InventorWork')
            open_inv()
            return True
        else:
            raise OSError('Inventor not closed')

def make(project,machine):
    if kill():
        if rename():
            newIW(project, machine)
            return True
        else:
            return False
    else:
        return False
    

##Close current inventor session

def kill():
    handle = WindowEnumerate()
    if not handle:
        return True
    win32gui.SetForegroundWindow(handle)
    win32gui.SendMessage(handle,win32con.WM_CLOSE,0,0)  #waits for message to be processed
    if not WindowEnumerate():
        return True
    else:
        return False

#windows enumeration handler functions, enumerates windows to get handlers
    #then gets window names
    #adapted from: https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def WindowEnumerate():
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if 'Autodesk Inventor Professional' in i[1]:
            return i[0]
    return False
    

def open_inv():
    p = subprocess.Popen('C:\\Program Files\\Autodesk\\Inventor 2016\\Bin\\Inventor.exe');
    time.sleep(5);



#Rename current inventorwork folder to match folder_name.txt
def rename():
    txtpath = 'C:\\InventorWork\\folder_name.txt'
    folder_txt = open(txtpath)
    source_name = folder_txt.read()
    folder_txt.close()
    time.sleep(1)
    result = False
    #loading window for rename, if folder is locked
    while not result:
        try:
            os.rename('C:\\InventorWork', 'C:\\' + source_name)
            result = True
        except PermissionError:
            time.sleep(0.5)
            continue
    return True


def newIW(project, machine):
    p_name = 'InventorWork_' + project.replace(' ', '') + '_' + machine.replace(' ', '') # strips input spaces formates to _project_machine
    batf = 'M:\\Project Engineering\\ENGDATA\\Reference Data\\Dev and Training Resc\\cad\\30 Inventor\\New InventorWork.bat'
    os.startfile(batf)         #inventor must be opened to generate project file in IW
    time.sleep(2)       #sleep buffer to make sure project file is generated, not sure if required?
    no_proj(project,machine, None)
    open_inv()
    return 'done newIW'

def no_proj(project,machine, folder):
    #if folder name input, generate folder_name.txt file in folder input
    if folder != None:
        destination_path = 'C:\\' + folder
        open(destination_path + '\\folder_name.txt', 'a+')
        folder_txt = open(destination_path + '\\folder_name.txt', 'w')
        folder_txt.write(folder)
        folder_txt.close
    #else generate txt from project and machine input
    else:
        open('C:\\InventorWork\\folder_name.txt', 'a+')
        folder_txt = open('C:\\InventorWork\\folder_name.txt', 'w')
        folder_txt.write('InventorWork_' + project + '_' + machine)
        folder_txt.close
    
def check_valid_folder_name(name):
    for i in name:
        if ord(i) > 64 and ord(i) < 91:
            continue
        if ord(i) > 96 and ord(i) < 123:
            continue
        if ord(i) > 47 and ord(i) < 58:
            continue
        if ord(i) == 95 or ord(i) == 32:
            continue
        else:
            return False
    return True

def rename_folder(project: str, machine:str, folder:str) -> None:
    with open(f"C:\\{folder}\\folder_name.txt", 'w+') as txtfile:
        txtfile.write(f"InventorWork_{project}_{machine}")
    if folder != 'InventorWork':
        os.rename(f"C:\\{folder}", f"C:\\InventorWork_{project}_{machine}")
    else:
        pass


        
        
        

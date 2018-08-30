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
        print('no txt file')
        raise LookupError('Cannot find folder_name.txt')
    #check for folder_name in destination folder

    #TO IMPLEMENT
    '''
    if os.path.isfile(destination_path + '\\' + 'folder_name.txt'):
        pass
    else:
        no_proj(None, None, folder)     #create folder_name.txt with folder as name

    '''
    iw_change = 'C:\\' + folder
    if os.path.exists(iw_change):
        if kill():
            print('closed Inventor')
            rename()
            print('ran rename()')
            time.sleep(1)
            print(iw_change)
            time.sleep(1)
            os.rename(iw_change, 'C:\\InventorWork')
            print('renamed from' + iw_change)
            open_inv()
            print('opened inventor')
            print('done')
            return True
        else:
            print('inventor not closed')
            raise OSError('Inventor not closed')

def kill():
    handle = WindowEnumerate()
    print(handle)
    if not handle:
        print('inventor already closed')
        return True
    win32gui.SetForegroundWindow(handle)
    win32gui.SendMessage(handle,win32con.WM_CLOSE,0,0)  #waits for message to be processed
    if not WindowEnumerate():
        print('kill returning True')
        return True
    else:
        print('kill returning False')
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
            print(i)
            return i[0]
    return False
    

def open_inv():
    p = subprocess.Popen('C:\\Program Files\\Autodesk\\Inventor 2016\\Bin\\Inventor.exe');
    print('opened inventor')
    print(p.poll() == None);
    time.sleep(5);
    print(p.poll() == None);

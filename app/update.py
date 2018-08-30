###Change IW

import os
#from app import app

def update_folder_list():
    folder_list =[]
    for i in os.listdir('C:\\'):
        if 'InventorWork' in i:
            folder_list.append(i)
    return folder_list

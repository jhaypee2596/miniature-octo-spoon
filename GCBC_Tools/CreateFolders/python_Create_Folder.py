import os

#Location Folder to Create Folders  
root_path = 'D:\\Fernando\\Downloads\\temp\\pythonCreateFolder'

#List of Folders to be Created   
list = ['car', 'truck', 'bike', 'cycle', 'train']

for items in list:
    path = os.path.join(root_path, items)
    os.mkdir(path)

rootdir = 'D:/Fernando/Downloads/temp/pythonCreateFolder'
for it in os.scandir(rootdir):
    if it.is_dir():
        path_txt_1 = it.path.replace("\\","/")
        path_txt_2 = path_txt_1.replace("/", "\\\\")
        #print(it.path)
        print(path_txt_2)
        #Create Folders 
        for items in list:
            path = os.path.join(path_txt_2, items)
            os.mkdir(path)



# file-organizer.py
import os, shutil
folder = input("Enter folder path to organize: ")
if not os.path.exists(folder): print("Invalid folder!"); exit()
for f in os.listdir(folder):
    fpath=os.path.join(folder,f)
    if os.path.isfile(fpath):
        ext=f.split('.')[-1]; d=os.path.join(folder,ext)
        os.makedirs(d, exist_ok=True); shutil.move(fpath, d)
print("Files organized by extension!")

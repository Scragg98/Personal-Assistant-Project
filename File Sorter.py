import os, shutil
from win11toast import toast

#Sets the folder path#
Path = r"C:\Users\Lukes\Downloads"

#Loops over files in path and splits files into file name and file extension#
for file in os.listdir(Path):
    name, ext = os.path.splitext(file)
    os.chdir(Path)
    #Moves guitar tabs to Google Drive#
    if ext == ".gp4" or ext == ".gp5":
        print(file)
        shutil.move(os.path.join(Path,file), "G:\My Drive\Guitar resources\Guitar tabs")
        toast("Successfully moved guitar tabs to Google Drive", on_click='G:\My Drive\Guitar resources\Guitar tabs')
    #Moves ".exe" files to dedicated folder. If folder doesn't exist, it is created#
    elif ext == ".exe":
        if not os.path.exists("Application Setup Files"):
            os.mkdir("Application Setup Files")
        else:
            shutil.move(os.path.join(Path,file), "Application Setup Files")
    elif ext == ".jpg" or ext == ".png":
        shutil.move(os.path.join(Path,file), r"C:\Users\Lukes\Pictures")
    elif ext == ".pdf" or ext == ".PDF":
        if not os.path.exists("PDFs"):
            os.mkdir("PDFs")
        else:
            shutil.move(os.path.join(Path,file), "PDFs")
    elif ext == ".docx":
        if not os.path.exists("Word Docs"):
            os.mkdir("Word Docs")
        else:
            shutil.move(os.path.join(Path,file), "Word Docs")
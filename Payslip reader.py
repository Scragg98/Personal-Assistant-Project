import os, shutil
from PyPDF2 import PdfReader

path = r"G:\My Drive\Banking & budgets\Budgets"


for subdir, dirs, files in os.walk(path):
    for fname in files:
        name, ext = os.path.splitext(fname)
        if ext == "":
            file_and_path = os.path.join(subdir, fname)
            path_elements = file_and_path.split("\\")
            if "2020" not in path_elements[-1] and "2019" not in path_elements[-1]: 
                print(file_and_path)
                os.rename(file_and_path, os.path.join(name +" " + path_elements[-3] + ".pdf"))


#reader = PdfReader(r'G:\My Drive\Banking & budgets\Budgets\2022\Payslips\1 - January payslip.pdf')

#f = open("demofile2.txt", "a")
#page = reader.pages[0]
#print(page.extract_text())
#f.write(page.extract_text())
#f.close()

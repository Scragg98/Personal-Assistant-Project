import os, shutil, pdfplumber

Path = r"G:\My Drive\Banking & budgets\Budgets"

for f in os.walk(Path):
    print(f)
    
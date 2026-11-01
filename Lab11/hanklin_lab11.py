
# 95896-A, 2026 Fall
# Student Name: Hank Lin
# Andrew ID: hanklin

'''1. Display the following information:
The current working directory using os.getcwd()
The current date and time using datetime.now()
The current UNIX timestamp using time.time()'''


import os, time
from datetime import datetime

directory = os.getcwd()
print("Current working directory:", directory)

t_now= datetime.now()
print("Current time:", t_now)

t_unix = time.time()
print("Current UNIX timestamp:", t_unix)

t_formatted = t_now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", t_formatted)

#%%
'''2. Create a directory called Lab11 using the mkdir() method. 
If it already exists, simply display a message 
indicating that it already exists instead of crashing.
Change into this directory using os.chdir(). Display the
current directory again to verify the change.
'''
# import os

# os.chdir(r"C:\Users\chihh")
# print(os.getcwd())

try:
    os.mkdir("Lab11")
except FileExistsError:
    print("Lab11 already exists.")

os.chdir("Lab11")
print("Current working directory:", os.getcwd())


#%%
'''3. Create a text file named student.txt using the with open method.
Write your name, today’s date, and your favorite programming language.
Make sure that between line of information, you add a blank line (i.e. new
line). '''

'''Create another directory called Backup. 
Use shutil.copy() to copy student.txt into the Backup directory. 
Display a message indicating the copy was successful. For now, Backup should be in the Lab13
directory. '''

import os
import shutil
from datetime import datetime

fd = os.open("student.txt", os.O_WRONLY | os.O_CREAT)

data = "Hank Lin\n\n2026-10-05\n\nPython\n"

byteData = data.encode("utf-8")

os.write(fd, byteData)

os.close(fd)

try:
    os.mkdir("Backup")
except FileExistsError:
    print("Backup already exists.")

shutil.copy("student.txt", "Backup")

print("Copy successful.")


#%%
'''4. Rename student.txt to studentInfo.txt using shutil.move() . 
Verify that the renamed file exists.'''

shutil.move("student.txt", "studentInfo.txt")

if os.path.exists("studentInfo.txt"):
    print("studentInfo.txt exists.")
else:
    print("Rename failed.")

#%%
'''5. Use os.walk() beginning with the current directory. 
Display the directory and the corresponding file in each directory with a label.
Try it with other directories on your computer to see a more complicated structure. 
'''
import os

for root, listing, filenames in os.walk("."):
    print("Directory:", root)
    print("Files:", filenames)

#%%
''' 6. Using pathlib.Path, display information about the renamed file.
Print the file name, extension, and parent directory.
Also display every directory located inside the current directory using Path.iterdir(). 
'''
from pathlib import Path

path = Path.cwd()
file = path / "studentInfo.txt"

print("Name:", file.name)
print("Extension:", file.suffix)
print("Parent:", file.parent.name)

print("Directories:")
for item in path.iterdir():
    if item.is_dir():
        print(item.name)

#%%
''' 7. Run the command python3 <filename you are running> hello world 123
and then use the sys.argv method to display the command line arguments 
which in this case is the filename, hello, world, and 123.
'''
import sys

print(sys.argv)


#%%
''' 8. open studentInfo.txt for reading
sys.stdout.write()
sys.stderr.write()
'''

import sys

with open("studentInfo.txt", "r") as f:
    for line in f:
        if line.strip():
            sys.stdout.write(line)
        else:
            sys.stderr.write("Warning: Blank line found.\n")




wrong_lab = Path(r"C:\Users\chihh\Lab11")

if wrong_lab.exists():
    for item in wrong_lab.rglob("*"):
        print(item)
        
        

#%% Q9
import zipfile
from pathlib import Path

# Create Lab11.zip
with zipfile.ZipFile("Lab11.zip", "w") as zip_file:
    zip_file.write(
        "studentInfo.txt",
        arcname="studentInfo.txt"
    )

    zip_file.write(
        "Backup/student.txt",
        arcname="Backup/student.txt"
    )

# Extract Lab11.zip
with zipfile.ZipFile("Lab11.zip", "r") as zip_file:
    zip_file.extractall("ExtractedLab11")

# Verify extracted files
file1 = Path("ExtractedLab11/studentInfo.txt")
file2 = Path("ExtractedLab11/Backup/student.txt")

print(f"Extracted file {file1} exists: {file1.exists()}")
print(f"Extracted file {file2} exists: {file2.exists()}")

all_extracted_files_exist = file1.exists() and file2.exists()
print(f"All extracted files exist: {all_extracted_files_exist}")



import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current Working Directory:", os.getcwd())
print(__file__)
filename = input("Enter File Name!")
try:
    file = open(filename, "r")
except PermissionError as pe:
    print(f"{pe}")
except FileNotFoundError as fnfe:
    print(f"{fnfe}")

else:
    three_lines = file.readlines()[0:3]
    if not three_lines:
        print("File is empty.")
    for ln in three_lines:
        print(ln)
    file.close()
finally:
    print("File operation attempted.")
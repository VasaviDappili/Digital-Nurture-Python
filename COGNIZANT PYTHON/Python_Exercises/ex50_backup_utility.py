import shutil

try:
    shutil.copy("sample.txt", "backup_sample.txt")
    print("Backup Created")

except FileNotFoundError:
    print("Source File Not Found")
import os
import shutil

baseDir = 'Your_File_Path_Here' # Location of directory you want to filter
listedDir = os.listdir(baseDir)          # List/Array of all the files in given directories (including sub-directories)

files = []

# Loop through the listedDir list/array ignoring any directories and putting all the files in a seperate list
def filterFiles():
    for file in listedDir:
        split_file = os.path.splitext(file)
        file_ext  = split_file[1]

        if len(file_ext) == 0:
            print('Ignoring Directory.......')
        else: 
            files.append(file)

filterFiles()

# File extensions 
imageExt    = ['.jpg',  '.png',  'gif', '.jpeg']
docExt      = ['.pdf', '.docx',  'txt']
vidExt      = ['.mp4',  '.avi', '.mov']
zipExt      = ['.rar',  '.zip', '7zip']
exeExt      = ['.exe',  '.bat']

file_extentions = {
    'image': imageExt,
    'document': docExt,
    'video': vidExt,
    'zip': zipExt,
    'exe': exeExt,
}

# Loop through the files list/array
for file in files:
    split_file = os.path.splitext(file)
    file_ext  = split_file[1].lower()
    # loop through the file_extensions dictionary and create directories if they dont exist yet and move the respective files to them
    for category, extensions in file_extentions.items():
        if file_ext in extensions:
            source_file_path = os.path.join(baseDir, file)
        
            target_folder = os.path.join(baseDir, category.capitalize())
            os.makedirs(target_folder, exist_ok=True)

            target_file_path = os.path.join(target_folder, file)

            try:
                shutil.move(source_file_path, target_file_path)
                print(f"Moved {file} to {category.capitalize()}/")
            except FileNotFoundError as e:
                print(print(f"Error moving file {file}: {e}"))
            break 

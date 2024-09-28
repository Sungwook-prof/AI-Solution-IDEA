import os
import random
import shutil
import json
import glob

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            ext = filepath[-3:].lower()
            if ext == 'jpg' or ext == 'png':
                file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

img_dir = 'C:\\work\\yolov9\\data\\coco\\images\\train\\'
img2_dir = 'C:\\work\\yolov9\\data\\coco\\images\\test\\'
img3_dir = 'C:\\work\\yolov9\\data\\coco\\images\\val\\'

directory = img_dir

file_paths = []  # List which will store all of the full filepaths.

# Walk the tree.
for root, directories, files in os.walk(directory):
    for filename in files:
        # Join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        ext = filepath[-3:].lower()
        if ext == 'jpg' or ext == 'png':
            file_paths.append(filepath)  # Add it to the list.

img_list = file_paths

fn = 'C:\\work\\yolov9\\data\\coco\\train.txt'
with open(fn, 'w') as f:
    for i in img_list:
        ii  = os.path.split(i)[1]
        str = './images/train/'+ii+'\n'
        f.write(str)
        
        
directory = img2_dir

file_paths = []  # List which will store all of the full filepaths.

# Walk the tree.
for root, directories, files in os.walk(directory):
    for filename in files:
        # Join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        ext = filepath[-3:].lower()
        if ext == 'jpg' or ext == 'png':
            file_paths.append(filepath)  # Add it to the list.

img_list = file_paths

fn = 'C:\\work\\yolov9\\data\\coco\\test.txt'
with open(fn, 'w') as f:
    for i in img_list:
        ii  = os.path.split(i)[1]
        str = './images/test/'+ii+'\n'
        f.write(str)
        
directory = img3_dir

file_paths = []  # List which will store all of the full filepaths.

# Walk the tree.
for root, directories, files in os.walk(directory):
    for filename in files:
        # Join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        ext = filepath[-3:].lower()
        if ext == 'jpg' or ext == 'png':
            file_paths.append(filepath)  # Add it to the list.

img_list = file_paths

fn = 'C:\\work\\yolov9\\data\\coco\\val.txt'
with open(fn, 'w') as f:
    for i in img_list:
        ii  = os.path.split(i)[1]
        str = './images/val/'+ii+'\n'
        f.write(str)
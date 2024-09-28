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

img_dir = 'C:\\work\\yolov9\\data\\coco\\images\\'
lbl_dir = 'C:\\work\\yolov9\\data\\coco\\labels\\'

# 카테고리 생성. images와 labels 아래에 있어야 함
split_cat = ['val', 'train', 'test']

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
l = len(img_list)
random.shuffle(img_list)
val_cnt = l // 10
train_cnt = val_cnt*8
test_cnt = l - val_cnt - train_cnt

img_list = get_filepaths(img_dir)
train_cnt += val_cnt
num = 0
save_cnt = 0

for i in img_list:
    # if save_cnt > 10:
    #     break
    ii  = os.path.split(i)[1]
    # print(ii)
    label_name = ii[:-4] + '.txt'
    
    dest_name = img_dir
    if num < val_cnt:
        dest_name += split_cat[0] + '/' + ii
    elif num < train_cnt:
        dest_name += split_cat[1] + '/' + ii
    else:
        dest_name += split_cat[2] + '/' + ii
    # Define the source and destination paths

    # Copy the file
    shutil.move(i, dest_name)
    
    dest_name = lbl_dir
    if num < val_cnt:
        dest_name += split_cat[0] + '/' + label_name
    elif num < train_cnt:
        dest_name += split_cat[1] + '/' + label_name
    else:
        dest_name += split_cat[2] + '/' + label_name
    # Define the source and destination paths

    src_name = lbl_dir + label_name
    # Copy the file
    shutil.move(src_name, dest_name)
    
    num += 1

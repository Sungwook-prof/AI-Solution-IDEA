import os
import random
import shutil
import json
import glob

'''24: backpack
25: umbrella
26: handbag
27: tie
41: cup
42: fork
43: knife
44: spoon'''

cat ={'24':'0','25':'1','26':'2','27':'3','41':'4','42':'5','43':'6','44':'7'}
dog ={}

def get_filepaths(directory):
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

train_dir = '/home/yuji/person_data/opendata/Training/'
val_dir = '/home/yuji/person_data/opendata/Training/'
train_lbl = '/home/yuji/person_data/opendata/Training/' 
val_lbl = '/home/yuji/person_data/opendata/Training/'

base_img_dir = 'C:\\work\\yolov9\\data\\coco\\origin\\images'
base_lbl_dir = 'C:\\work\\yolov9\\data\\coco\\origin\\labels\\'

img_dir = 'C:\\work\\yolov9\\data\\coco\\images\\'
lbl_dir = 'C:\\work\\yolov9\\data\\coco\\labels\\'

# 카테고리 생성. images와 labels 아래에 있어야 함
split_cat = ['val', 'train', 'test']

directory = base_img_dir

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
#random.shuffle(img_list)
val_cnt = l // 10
train_cnt = val_cnt*8
test_cnt = l - val_cnt - train_cnt

#img_list = get_filepaths(img_dir)
train_cnt += val_cnt
num = 0
print("total fine number: ", l, "\n")
save_cnt = 0
pr_sc = 0

objs = dict()
obj_names = ['backpack', 'umbrella', 'handbag', 'tie', 'cup', 'fork', 'knife', 'spoon']

for i in img_list:
    # if save_cnt > 10:
    #     break
    ii  = os.path.split(i)[1]
    
    # print(ii)
    label_name = ii[:-4] + '.txt'
    
    fol = os.path.split(i)[0].split('\\')
    #print(fol[-1])
    
    lbl_name = base_lbl_dir + fol[-1] + '\\' + label_name
    #print(lbl_name)
    
    try:
        with open(lbl_name, 'r') as f:
            lst = f.readlines()
            lst2 = []
            for ll in lst:
                ll2 = ll.split()                        
                if ll2[0] in cat.keys():
                    lst2.append(ll2)
                    
                    
            if len(lst2) > 0:
                # copy image
                dest_name = img_dir + ii
                shutil.copyfile(i, dest_name)
                
                # create txt
                dest_name = lbl_dir + label_name
                with open(dest_name, 'w') as f2:
                    for ll in lst:
                        ll2 = ll.split()
                        if ll2[0] in cat.keys():
                            st = cat[ll2[0]]
                            objs[cat[ll2[0]]] = objs.get(cat[ll2[0]], 0) +1
                            for i2 in range(1, len(ll2)):
                                st += ' ' + ll2[i2]
                            st += '\n'
                            f2.write(st)
                      
                save_cnt += 1      
                
    except FileNotFoundError: continue
    
    if pr_sc != save_cnt and save_cnt % 1000 == 0: print('processed iamges :', save_cnt)
    pr_sc = save_cnt
    
print('-'*20)
print('Total saved files:', save_cnt)
for i in objs:
    print(obj_names[int(i)], '=', objs[i])
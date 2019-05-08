import os
my_dir=""
'''"003-build_pos_dir.py"
builds the renaming directories.
The out_dirs are used to hold the finished images,
from which processing will start.
'''
def make_dirs(my_dir):
    print("Entering make_dirs with my_dir=",my_dir)
    if not os.path.exists(my_dir):
        print("IF: this path does not exist",my_dir)
        os.makedirs(my_dir)
    else:
        print("This path exists:", my_dir)

#####################################################
# M A I N  L O G I C
#####################################################
data_dir = '/root/opencv_python/data/' #Holds final outputs of processp
info_dir = '/root/opencv_python/info/' #Holds processed pos images used for training 
in_dir   = '/root/opencv_python/in_pos/'#The pos dir for grayscale pos images
out_neg_dir   = '/root/opencv_python/out_neg/' #The neg dir for gray and scaled neg images
out_dir   = '/root/opencv_python/out_pos/' #The pos dir for gray and scaled pos images
raw_dir  = '/mnt/usb/raw_pos/'         #Hold the pristing pos images

for my_dir in data_dir, info_dir, in_dir, out_neg_dir, out_dir, raw_dir:
    make_dirs(my_dir)

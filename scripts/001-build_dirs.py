import os
main_dir="/root/opencv_python"
my_dir=""

'''"001-build_dirs.py"
builds the renaming directories.
The out_dirs are used to hold the finished images,
from which processing will start.
'''
def make_dirs(my_dir):
    if not os.path.exists(my_dir):
        print("INFO: Creating directory:",my_dir)
        os.makedirs(my_dir)
    else:
        print("INFO: Skipping", my_dir, "This path exists.")

#####################################################
# M A I N  L O G I C
#####################################################
log_dir  = main_dir + "/" + 'logs/'  #Place to hold our runtime logs
data_dir = main_dir + "/" + 'data/' #Holds final outputs of processp
info_dir = main_dir + "/" + 'info/' #Holds processed pos images used for training 
in_dir   = main_dir + "/" + 'in_pos/'#The pos dir for grayscale pos images
out_neg_dir   = main_dir + "/" + 'out_neg/' #The neg dir for gray and scaled neg images
out_dir  = main_dir + "/" + 'out_pos/' #The pos dir for gray and scaled pos images
raw_dir  = '/mnt/usb/raw_pos/'         #Hold the pristing pos images

for my_dir in log_dir, data_dir, info_dir, in_dir, out_neg_dir, out_dir, raw_dir:
    make_dirs(my_dir)

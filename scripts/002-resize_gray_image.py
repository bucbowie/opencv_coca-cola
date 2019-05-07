import urllib
import cv2
import numpy as np
import os
import errno

'''002-if-000-fails-resize.py reads in 
a list of images and does 2 things:
    1. Change image to grayscale
    2. Resize image to 100x100 - size for neg. images
'''
#--------------------------------#
def check_directories(in_dir):
#--------------------------------#
    if not os.path.exists(in_dir):
        print("Error: 002-if-000-fails-resize.py \n--------------------------------#\nThe needed input directory: {0}\ndoes not exist and impedes running this program.\nEnsure directory {0} exists, is readable,\n".format(in_dir))
        raise ValueError("Unable to find or access needed input ==>",  in_dir)

#--------------------------------#
def ensure_directories(my_dir):
#--------------------------------#
    if not os.path.exists(my_dir):
        os.makedirs(my_dir)

#--------------------------------#
def scrap_raw():
#--------------------------------#
    
    for jpg in os.listdir(scrape_dir):
        try:
            print("INFO: Processing image", scrape_dir + "/"  + jpg, "of size", os.path.getsize(scrape_dir + "/" + jpg))
            if os.path.getsize(scrape_dir + "/" + jpg) > size_smallest_img:
                img = cv2.imread(scrape_dir + "/"  + jpg, cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(img, (100, 100))
                cv2.imwrite(in_dir + "/" + jpg, resized_image)
            else:
                print("WARNING: Skipping image",scrape_dir + "/"  + jpg, "of size", os.path.getsize(scrape_dir + "/" + jpg))
        except Exception as e:
            print(str(e))

#################################################
# M A I N   L O G I C
#################################################
#
#Define variables
#
size_smallest_img = (1024 * 5)   #Any image smaller considered blank or corrupt, we will skip these.
scrape_dir =  '/mnt/usb/raw_neg' #The place to store the freshly scraped images.
in_dir =  '/mnt/usb/in_neg'  #Formatted negative images which will feed 'out_neg.' 
#
#Ensure inputs and outputs exists
check_directories(scrape_dir)        #Ensure inputs exist before running main logix.
ensure_directories(in_dir)   #Ensure the output directory is defined to hold outputs.
#
#Process images: reading from input; write to output.
#
scrap_raw()            #Read each image, grayscale and resize - write to outdir.

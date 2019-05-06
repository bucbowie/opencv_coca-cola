import urllib
import cv2
import numpy as np
import os
''' 001-if-000-fails_url_list.py pulls
images from the intenet - image-net.org.
The url selection comes from a list stored
locally and each line in the url list is 
read and program attempts to find and download 
save image locally. If you are running this
multiple time, be sure to set the pic_num
variable so it does not overwrite existing 
images'''

#--------------------------------#
def check_directories(in_dir):
#--------------------------------#
    if not os.path.exists(in_dir):
        print("Error: 001-if-000-fails_url_list.py \n--------------------------------#\nThe needed input directory: {0}\ndoes not exist and impedes running this program.\nEnsure directory {0} exists, is readable,\n".format(in_dir))
        raise FileNotFoundError

#--------------------------------#
def ensure_directories(my_dir):
#--------------------------------#
    if not os.path.exists(my_dir):
        os.makedirs(my_dir)

#--------------------------------#
def scrap_raw(my_list_of_url):
#--------------------------------#
    with open(my_list_of_url, 'r') as url_url:
        pic_num  = 1
        for i in url_url:
            try:
                print("INFO: Processing URL " + i)
                urllib.urlretrieve(i,  scrape_dir + "/" +   str(pic_num) + ".jpg")
                if os.path.getsize(scrape_dir + "/" + str(pic_num) + ".jpg") > size_smallest_img:
                    pic_num += 1

            except Exception as e:
                print(str(e))

#################################################
# M A I N   L O G I C
#################################################
size_smallest_img = (1024 * 5)         #The miniumum size of images we will accept. If smaller, assume does not exist of corrupt.
my_list_of_url = '/mnt/usb/urls/people.url' #The file holding the url list of images we want to download.
scrape_dir =  '/mnt/usb/raw_neg'       #The place to store the freshly scraped images
check_directories(my_list_of_url)      #Ensure inputs exist before processing.
ensure_directories(scrape_dir)         #Create directories if they do not exist
scrap_raw(my_list_of_url)              #Pull images from image-net.org

# loading files - fast
from load_fastest import load_files
load_files('Orignal_Images')

# loading dependecies
import cv2
from bg_remover import bg_remover
from bg_changer import bg_changer

# setting path
orig_img_path = 'Orignal_Images/view2.jpeg '
bgr_img_path = 'Background_Images/pic_3.jpeg '

# use functions
bg_remover(img_path=orig_img_path, img_name='file.jpeg')
bg_changer(inp_img_path=orig_img_path, bg_img_pathgr_img_path, img_name='file_2.jpeg')
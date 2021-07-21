'''
Function TO Change Background
'''
# Loading dependencies
import pixellib
import cv2
from pixellib.tune_bg import alter_bg


def bg_changer(inp_img_path, bg_img_path , img_name = None):
    '''
    Takes in Input Image Path and Output Image Path and Image Name, removes background , and changes background of orignal images
    :return: nothing
    '''
    change_bg = alter_bg() # instantiate object
    change_bg.load_pascalvoc_model('deeplabv3_xception_tf_dim_ordering_tf_kernels.h5')
    output = change_bg.change_bg_img(f_image_path=inp_img_path, b_image_path=bg_img_path,output_image_name=img_name+"bg_change.jpeg")
    cv2.imwrite("Created_Images/Bg_Changed/" + img_name + "_bg_remove.jpeg", output)

bg_changer(inp_img_path='Orignal_Images/view2.jpeg', bg_img_path='Background_Images/pic_1.jpeg', img_name='view_2')
bg_changer(inp_img_path='Orignal_Images/view3.jpeg', bg_img_path='Background_Images/pic_2.jpeg', img_name='view_3')
bg_changer(inp_img_path='Orignal_Images/view4.jpeg', bg_img_path='Background_Images/pic_3.jpeg', img_name='view_4')

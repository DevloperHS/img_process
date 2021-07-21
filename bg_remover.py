'''
Function TO Remove Background

I used PixelLib: PixelLib is a library created to ensure easy integration of image segmentation in real life.
'''

# Note - Must Have - deeplabv3_xception_tf_dim_ordering_tf_kernels.h5 file in folder
# as it is the main model which will be used to do segmentation and then mask it on a color background - black

# Loading dependencies
import pixellib
import cv2
from pixellib.tune_bg import alter_bg

#creating a function and removes background + save

def bg_remover(inp_img_path, img_name):
    '''
    Takes in Input Image Path and Output Image Path and Image Name, removes background ,then mask orignal mask and saves it
    :return: nothing
    '''
    change_bg = alter_bg() # instantiate object
    change_bg.load_pascalvoc_model('deeplabv3_xception_tf_dim_ordering_tf_kernels.h5')
    output = change_bg.color_bg(image_path=inp_img_path, colors = (0,0,0) ,output_image_name=img_name+"bg_remove.jpeg")
    cv2.imwrite("Created_Images/Bg_Removed/"+img_name+"_bg_remove.jpeg", output)
    
# sample check    
'''
bg_remover(inp_img_path='Orignal_Images/view2.jpeg', img_name='view2.jpeg')
bg_remover(inp_img_path='Orignal_Images/view3.jpeg', img_name='view3.jpeg')
bg_remover(inp_img_path='Orignal_Images/view4.jpeg', img_name='view4.jpeg')
'''

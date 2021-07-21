# cARScan.ai
This repositiory  is for the project given to me by carscan.ai


REQUIREMENTS:
---------------------------------------------------------
1. Clone this repository 
 ``` git clone https://github.com/DevloperHS/cARScan.ai.git ```
2. Get the model file from https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5
  and place it in same directory[```cARScan.ai-main```] 
3. Go to terminal , change to directory where files are stored [```cARScan.ai-main```] 

USAGE:
-----------------------------------------------------
 1. Load all the orignal img files in **Orignal_Images** folder
 2. Load all the background img files im **Background_Images** folder
 3. Create a new python file in same directory / refer ```demo.py``
 ```
Load Dependency
import cv2
from bg_remover import bg_remover # import bg_remover
from bg_changer import bg_changer # import bg_changer
from load_fastest import load_files

# load files
load_files('path = Orignal_Images') 

# set path
orig_img_path = 'Orignal_Images/view2.jpeg' # path to orignal image
bgr_img_path = 'Background_Images/pic_3.jpeg'  path to background image
```
* Note currently the function can hold a single path for both parameters

 ```
 #for removing background 
 bg_remover(img_path=orig_img_path, img_name='file.jpeg') # image_name - name given to image
 ```
* Output can be found in **Created_Images/Bg_Removed**
* for more control over back ground change the ```colors = (0,0,0)``` parameter of **bg_remover.py** file

```
# for changing background
bg_changer(inp_img_path=orig_img_path, bg_img_path= bgr_img_path, img_name='file_2.jpeg') 
```
* Output can be found in **Created_Images/Bg_Changed**

If you have suggestion feel free to let me know and for changes use pull request

Sample Files
Orignal Image:
![Orignal Image](https://user-images.githubusercontent.com/74095712/126471194-1caed3ae-5e17-43d1-b507-29d18a2a8e9a.jpeg)

Removed Background :
![Removed Background](https://user-images.githubusercontent.com/74095712/126470803-de216a76-78c7-4df7-8de8-aa0638114d66.jpeg)

Changed background :
![Changed Background](https://user-images.githubusercontent.com/74095712/126470990-112b8d60-7333-4c7a-bb45-77d4b495a7bb.jpeg)

'''
- Loading Files - Fastest Way Using Glob Module
'''
# loading dependencies
import cv2
import os
import glob
from functools import wraps
from time import time

# function to check timing
def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Elapsed time: {} ms'.format(round(end-start, 2)))
        return result
    return wrapper

# load Files
@timing
def load_files(path):
    orig_img_dir = path
    data_path = os.path.join(orig_img_dir,'*g')
    files = glob.glob(data_path)
    data = []
    for f1 in files:
        img = cv2.imread(f1)
        data.append(img)
    return  data
'''
imgs = load_files('Orignal_Images')

for i in imgs:
    cv2.imshow('Loaded Images', i)
    cv2.waitKey(0)

print(imgs)
'''
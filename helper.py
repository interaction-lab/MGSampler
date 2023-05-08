import torch
from torch import nn
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import json

device = torch.device('cuda:0')

combined = cv2.imread('image_diff/img_00000.jpg' , 0)
tmpl = 'img_{:05}.jpg'

for i in range(1, 8):
    name = 'image_diff/'+tmpl.format(i)
    pic = cv2.imread(name , 0)
    combined += pic

plt.imsave('image_diff/combined.jpg',combined,cmap='gray')
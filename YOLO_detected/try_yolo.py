# -*- coding: utf-8 -*-
"""try_YOLO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CV_EibMCskl9N0Yx1r4NJRpawsMbImxy
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/AlexeyAB/darknet

# %cd /content/darknet
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!make
!wget https://pjreddie.com/media/files/yolov3.weights
#!./darknet detector train /content/darknet/data/your_data_file.data /content/darknet/cfg/your_custom_cfg_file.cfg /content/darknet/your_pretrained_weights.weights -dont_show
#!./darknet detector test /content/darknet/data/your_data_file.data /content/darknet/cfg/your_custom_cfg_file.cfg /content/darknet/your_trained_weights.weights path/to/your/image.jpg -thresh 0.5
import xml.etree.ElementTree as ET
import os
import cv2

def process_labels(label_id):

    in_file = open(DATASET_PATH + 'train.txt')
    out_file = open(DATASET_PATH + 'processed_train.txt', 'w')
    data = in_file.readlines()
    for line in data:
    	line = line[49:-5]
    	out_file.write(line + '\n')

if __name__ == '__main__':
    DATASET_PATH = "/home/cse-305/xwq_files/python_project/ssd.pytorch-master/data/VOCdevkit/VOC2007/ImageSets/Main/"
    process_labels(DATASET_PATH)
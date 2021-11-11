import os
from PIL import Image

images_path = '/home/cse-305/dataset/safety_helmet_paper/images'
txt_path = '/home/cse-305/dataset/safety_helmet_paper/labels'
xml_path = '/home/cse-305/dataset/safety_helmet_paper/xml'

new_images_path = '/home/cse-305/dataset/safety_helmet_paper/new_images'
new_txt_path = '/home/cse-305/dataset/safety_helmet_paper/new_labels'
new_xml_path = '/home/cse-305/dataset/safety_helmet_paper/new_xml'

filelists = os.listdir(images_path)
id = 00000

for item in filelists:
    image_name = images_path + '/' + item
    txt_name = txt_path + '/' + item[0:-4] + '.txt'
    xml_name = xml_path + '/' + item[0:-4] + '.xml'

    os.rename(image_name, new_images_path + '/' + str(id) + '.jpg')
    os.rename(txt_name, new_txt_path + '/' + str(id) + '.txt')
    os.rename(xml_name, new_xml_path + '/' + str(id) + '.xml')
    id += 1

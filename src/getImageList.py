import os
import numpy as np


def search(dirname):
    image_list = {}
    filenames = os.listdir(dirname)

    for filename in filenames:
        if(filename[0] != "."):
            full_filename = os.path.join(dirname, filename)
            images = os.listdir(full_filename)
            for image in images:
                image_list[filename] = os.path.join(full_filename, image)
                # print(filename, os.path.join(full_filename, image))
            

    return image_list
        

image_list = np.array(list(search("../../Caffe_data/").items(), dtype=dict(names = ['', '']])))

print(image_list)
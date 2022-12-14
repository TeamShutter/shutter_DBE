import numpy as np
import json
from photo.models import Photo
from tags.models import Tag

def similarity(vec_1, vec_2):
    vec_1 = np.array(vec_1)
    vec_2 = np.array(vec_2)
    vec_1_size = np.linalg.norm(vec_1, 2)
    vec_2_size = np.linalg.norm(vec_2, 2)
    vec_dot = np.dot(vec_1, vec_2)
    return vec_dot/(vec_1_size*vec_2_size)


def studio_vectorize(studio_obj):
    try:
        vector_size = 36
        tag_length = 17
        tag_color_length = 31

        photos = Photo.objects.filter(studio = studio_obj)
        vector = np.zeros(shape = (vector_size,))
        tag_num = 0
        for photo in photos:
            tags =photo.tags.all()
            for tag in tags:
                vector[tag.id-1] += 1
                tag_num += 1
            vector[photo.color + tag_length] += 1/len(photos)
            vector[photo.type + tag_color_length] += 1/len(photos)

        for i in range(18):
            vector[i] = vector[i]/tag_num
        return np.array(vector)
    except Exception as e:
        return print(str(e))
        
    
    


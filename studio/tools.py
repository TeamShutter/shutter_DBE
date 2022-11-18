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

# def json_reader():
#     with open('studio/studio_vector.json', 'rb') as f:
#         file_ = json.load(f)
#     return file_

# async def json_loader(new_studios, old_studios):
#     await waiter(new_studios, old_studios)

# async def waiter(new_studios, old_studios):
#     studios = new_studios+old_studios
#     with open('studio/studio_vector.json', 'w') as f:
#         json.dump(studios, f, indent=2)

def studio_vectorize(studio_obj):
    photos = Photo.objects.filter(studio = studio_obj)
    vector = np.zeros(shape = (23,))
    tag_num = 0
    for photo in photos:
        tags =photo.tags.all()
        for tag in tags:
            vector[tag.id-1] += 1
            tag_num += 1
        vector[photo.color+17] += 1/len(photos)
    for i in range(18):
        vector[i] = vector[i]/tag_num
    return np.array(vector)
        
    
    


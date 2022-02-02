from django.test import TestCase
import matplotlib.pyplot as plt
from deepface import DeepFace

img1_path = '/home/jamanbala_it/Рабочий стол/project_base/database/img1.jpeg'
img2_path = '/home/jamanbala_it/Рабочий стол/project_base/database/img5.jpg'

img1 = DeepFace.detectFace(img1_path)
img2 = DeepFace.detectFace(img2_path)

plt.imshow(img1)
plt.imshow(img2)
# print(plt)



model_name = 'ArcFace'
resp = DeepFace.verify(img1_path=img1_path, img2_path=img2_path, model_name=model_name)
print(resp)
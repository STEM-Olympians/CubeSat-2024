import numpy as np 
from PIL import Image
from tensorflow.keras.preprocessing import image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from keras.applications.vgg16 import VGG16
from sklearn.metrics.pairwise import cosine_similarity


embLayer = VGG16(weights='imagenet', include_top=False, 
              pooling='max', input_shape=(224, 224, 3))

for model_layer in embLayer.layers:
  model_layer.trainable = False

def load_image(image_path):
    """
        -----------------------------------------------------
        Process the image provided. 
        - Resize the image 
        -----------------------------------------------------
        return resized image
    """

    input_image = Image.open(image_path)
    resized_image = input_image.resize((224, 224))

    return resized_image

def get_image_embeddings(object_image : image):
    
    """
      -----------------------------------------------------
      convert image into 3d array and add additional dimension for model input
      -----------------------------------------------------
      return embeddings of the given image
    """

    image_array = np.expand_dims(image.img_to_array(object_image), axis = 0)
    image_embedding = embLayer.predict(image_array)

    return image_embedding

def get_similarity_score(first_image : str, second_image : str):
    """
        -----------------------------------------------------
        Takes image array and computes its embedding using VGG16 embedding model.
        -----------------------------------------------------
        return embedding of the image
        
    """

    first_image = load_image(first_image)
    second_image = load_image(second_image)

    first_image_vector = get_image_embeddings(first_image)
    second_image_vector = get_image_embeddings(second_image)
    
    similarity_score = cosine_similarity(first_image_vector, second_image_vector).reshape(1,)

    return similarity_score

def show_image(image_path):
  image = mpimg.imread(image_path)
  imgplot = plt.imshow(image)
  plt.show()

# define the path of the images
square1 = './Images/timessquare1.jpeg'
square2 = './Images/timessquare2.jpeg'
mit = './Images/MIT.jpeg'


THRESHOLD = 0.7
def trigger(before, after):
    """
        -----------------------------------------------------
        First step to recognize the images and return True/False based on the similarity score compared to the threshold constant.
        -----------------------------------------------------
        return similarity score
    """
    similarity_score = get_similarity_score(before, after)
    print(f"Similarity score: {similarity_score}")

    if similarity_score > THRESHOLD:
        return True
    else:
        return False

def building_segmentation(image):
    """
        -----------------------------------------------------
        Segment the image to identify the buildings and return the segmented image with bounded boxes!~
        -----------------------------------------------------
        return segmented image
    """
    print("Machine Learning model to be implemented here")

    img = load_image(image)
    
    # # Not sure if using the pre-embedded weights is better or not, but we can try both later
    # img_emb = get_image_embeddings(img)
    show_image(image)

    pass

def process(image1, image2):
    """
        -----------------------------------------------------
        Process the images and return the generated map if flood is detected, otherwise does nothing in nominal mode.
        -----------------------------------------------------
        return similarity score
    """
    triggered = trigger(image1, image2)
    
    if triggered:
        print("Flood detected")
        building_segmentation(image2)


        return True
    else:
        print("No flood detected")
        return False


process(square1, square2)
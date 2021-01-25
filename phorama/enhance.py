from PIL import Image
from phorama import models
import os
import numpy as np

class Enhancer:
    def __init__(self, model='SRGAN'):
        if not(model in ['SRGAN']):
            raise ValueError

        if model == 'SRGAN':
            self.model = models.SRGAN(os.path.dirname(__file__) + '/saved-models/SRGAN.h5')

    def enhance(self, image):
        image = np.asarray(image)
        image = self.model.predict(image)
        image = Image.fromarray(image)
        return image

        

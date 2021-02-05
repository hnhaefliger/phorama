from PIL import Image
from phorama import models
import os
import numpy as np

class Enhancer:
    '''Generalized class for image enhancement model.'''
    def __init__(self, model='SRGAN'):
        '''Initialize class with specified model.'''
        if not(model in ['SRGAN']):
            raise ValueError

        if model == 'SRGAN':
            self.model = models.SRGAN(os.path.dirname(__file__) + '/saved-models/SRGAN.h5')

    def enhance(self, image):
        '''
        Enhance an image.

        Input: PIL Image; Output: PIL Image
        '''
        image = np.asarray(image)
        image = self.model.predict(image)
        image = Image.fromarray(image)
        return image

        

import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D

class PhoramaModel:
    '''Generalized model class for phorama image enhancers.'''
    def __init__(self, load_path):
        '''Reconstruct model and load weights from specified path'''
        inputs = Input(shape=(None, None, 3))
        inner = inputs
        inner = Conv2D(3, (3,3), padding='same')(inner)
        
        self.model = Model(inputs=inputs, outputs=outputs)
        self.model.compile(loss='mse', optimizer='Adam')
        self.model.load_weights(load_path)

    def preprocess(self, data):
        '''Model-specific preprocessing from RGB image array.'''
        data = data / 255
        return data

    def postprocess(self, data):
        '''Model-specific postprocessing to recover an RGB image array.'''
        data = data * 255
        data = data.astype(np.uint8)
        return data

    def predict(self, data):
        '''Use model to predict from an RGB image array.'''
        data = self.preprocess(data)
        data = np.expand_dims(data, axis=0)
        data = self.model.predict(data)[0]
        data = np.array(data)
        data = self.postprocess(data)
        return data

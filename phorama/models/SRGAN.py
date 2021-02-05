import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, UpSampling2D, Activation, Add, BatchNormalization
from phorama.models.model import PhoramaModel

def ResidualBlock(inputs, filters):
    '''Residual convolutional block.'''
    x = Conv2D(filters, (3,3), strides=1, padding='same')(inputs)
    x = Activation('relu')(x)
    x = BatchNormalization(momentum=0.8)(x)
    x = Conv2D(filters, (3,3), strides=1, padding='same')(x)
    x = BatchNormalization(momentum=0.8)(x)
    x = Add()([x, inputs])
    return x

def DeConv2D(inputs):
    '''Block to double the input resolution as described in the SRGAN paper.'''
    x = UpSampling2D(size=2)(inputs)
    x = Conv2D(256, (3,3), strides=1, padding='same')(x)
    x = Activation('relu')(x)
    return x

class SRGAN(PhoramaModel):
    '''
    Model as described in the paper SRGAN.
    
    "Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network" (https://arxiv.org/pdf/1609.04802.pdf).
    '''
    def __init__(self, load_path):
        '''Construct the model and load weights from specified path.'''
        inputs = Input(shape=(None, None, 3))
        inner = inputs

        inner1 = Conv2D(64, (9,9), strides=1, padding='same')(inner)
        inner1 = Activation('relu')(inner1)

        inner = inner1
        inner = ResidualBlock(inner, 64)

        for _ in range(15):
            inner = ResidualBlock(inner, 64)

        inner = Conv2D(64, (3,3), strides=1, padding='same')(inner)
        inner = BatchNormalization(momentum=0.8)(inner)
        inner = Add()([inner, inner1])
        inner = DeConv2D(inner)
        outputs = Conv2D(3, (9,9), strides=1, padding='same', activation='sigmoid')(inner)

        self.model = Model(inputs=inputs, outputs=outputs)
        self.model.compile(loss='mse', optimizer='Adam')
        self.model.load_weights(load_path)

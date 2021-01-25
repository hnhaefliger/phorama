import tflite_runtime.interpreter as tflite
from PIL import Image
import os
import numpy as np

class Enhancer:
    def __init__(self, model='SRGAN', threads=1):
        if not(model + '.tflite' in os.listdir(os.path.dirname(__file__))):
            raise ValueError

        self.interpreter = tflite.Interpreter(model_path=os.path.dirname(__file__)+'/'+model+'.tflite', num_threads=threads)

    def enhance(self, image):
        width, heigth = image.size
        image = np.asarray(image) / 255
        image = np.expand_dims(image, axis=0)

        self.interpreter.resize_tensor_input(input_details[0]['index'], (1, height, width, 3))
        self.interpreter.allocate_tensors()

        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()

        self.interpreter.set_tensor(input_details[0]['index'], image)
        self.interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])
        
        image = np.squeeze(output_data) * 255
        image = Image.fromarray(image)

        

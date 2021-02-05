# phorama

A neural image enhancement library for python3

## Usage

```python3
import phorama
from PIL import Image

enhancer = phorama.Enhancer(model='SRGAN')
img = Image.open('path/to/input/image.jpg'
img = enhancer.enhance(img)
img.save('path/to/output/image.jpg')
```

## Examples

You might notice a few color patches. These are still being worked on.

![Demo 1](https://github.com/hnhaefliger/phorama/blob/main/images/image1_demo.jpeg)
![Demo 2](https://github.com/hnhaefliger/phorama/blob/main/images/image2_demo.jpeg)
![Demo 3](https://github.com/hnhaefliger/phorama/blob/main/images/image3_demo.jpeg)
![Demo 4](https://github.com/hnhaefliger/phorama/blob/main/images/image4_demo.jpeg)
![Demo 5](https://github.com/hnhaefliger/phorama/blob/main/images/image5_demo.jpeg)
![Demo 6](https://github.com/hnhaefliger/phorama/blob/main/images/image6_demo.jpeg)
![Demo 7](https://github.com/hnhaefliger/phorama/blob/main/images/image7_demo.jpeg)
![Demo 8](https://github.com/hnhaefliger/phorama/blob/main/images/image8_demo.jpeg)

## Models

***Models currently implemented***:

SRGAN (https://arxiv.org/pdf/1609.04802.pdf)

***Models to be implemented***:

UNet (https://arxiv.org/pdf/1505.04597.pdf)

RSGUNet (https://openaccess.thecvf.com/content_ECCVW_2018/papers/11133/Huang_Range_Scaling_Global_U-Net_for_Perceptual_Image_Enhancement_on_Mobile_ECCVW_2018_paper.pdf)

GVTNet (https://arxiv.org/pdf/2008.02340.pdf)

DPED (https://arxiv.org/pdf/1704.02470.pdf)

PyNet (https://arxiv.org/pdf/2002.05509.pdf)

CURL (https://arxiv.org/pdf/1911.13175.pdf)

FEQE (https://openaccess.thecvf.com/content_ECCVW_2018/papers/11133/Vu_Fast_and_Efficient_Image_Quality_Enhancement_via_Desubpixel_Convolutional_Neural_ECCVW_2018_paper.pdf)

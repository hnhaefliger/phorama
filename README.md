# phorama

Phorama is an neural image processing library for python3. At the moment it allows you to easily enhance your photos.

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

## Models

Models currently implemented:

SRGAN (https://arxiv.org/pdf/1609.04802.pdf)

Models to be implemented:

UNet (https://arxiv.org/pdf/1505.04597.pdf)

RSGUNet (https://openaccess.thecvf.com/content_ECCVW_2018/papers/11133/Huang_Range_Scaling_Global_U-Net_for_Perceptual_Image_Enhancement_on_Mobile_ECCVW_2018_paper.pdf)

GVTNet (https://arxiv.org/pdf/2008.02340.pdf)

DPED (https://arxiv.org/pdf/1704.02470.pdf)

PyNet (https://arxiv.org/pdf/2002.05509.pdf)

CURL (https://arxiv.org/pdf/1911.13175.pdf)

FEQE (https://openaccess.thecvf.com/content_ECCVW_2018/papers/11133/Vu_Fast_and_Efficient_Image_Quality_Enhancement_via_Desubpixel_Convolutional_Neural_ECCVW_2018_paper.pdf)

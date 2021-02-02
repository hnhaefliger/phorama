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

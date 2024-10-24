# imagepig
[Python package](https://pypi.org/project/imagepig/) for [Image Pig](https://imagepig.com/), the API for AI images.

## Installation

```
pip install imagepig
```

## Example of usage

```python
from imagepig import ImagePig

# create instance of API (put here your actual API key)
imagepig = ImagePig("your-api-key")

# call the API with a prompt to generate an image
result = imagepig.xl("cute piglet running on a green garden")

# save image to a file
result.save("cute-piglet.jpeg")

# or access image data (bytes)
result.data

# or access image as an object (needs to have the Pillow package installed)
result.image
```

## Contact us
Something does not work as expected? Feel free to [send us a message](https://imagepig.com/contact/), we are here for you.

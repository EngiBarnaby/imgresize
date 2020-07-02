from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill

# class Thumbnail(ImageSpec):
#     processors = [ResizeToFill(100, 100)]
#     format = 'JPEG'
#     options = {'quality': 60}

def make_resize(image, size=(100, 100)):
    im = Image.open(image)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    im = im.resize(size)
    thumb_io = BytesIO()
    im.save(thumb_io, 'JPEG', quality=95)
    image = File(thumb_io, name=image.name)
    return image


class UserImage(models.Model):
    image = models.ImageField(blank=False, null=False, upload_to='resize_img')
    height = models.IntegerField()
    weight = models.IntegerField()
    type = models.CharField(null=True, blank=True, max_length=10)

    def save(self, *args, **kwargs):

        self.image = make_resize(self.image, size = (self.height, self.weight))

        # source_file = open(self.image.url)
        # image_generator = Thumbnail(source=source_file)
        # result = image_generator.generate()
        # self.image = result
        # self.image = Thumbnail(self.image)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.image.url

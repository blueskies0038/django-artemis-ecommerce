from django.db import models
from store.models import *


class CollectionImage(models.Model):
    collection = models.ForeignKey("Collection", related_name="images", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        print('URL', url)
        return url

class CollectionPreview(models.Model):
    collection = models.ForeignKey("Collection", related_name="preview_images", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        print('URL', url)
        return url

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    credit = models.CharField(max_length=100)

    def __str__(self):
        return self.name
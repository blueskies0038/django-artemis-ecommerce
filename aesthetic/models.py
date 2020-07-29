from django.db import models

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    credit = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CollectionImages(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
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
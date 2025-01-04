import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True, default="default-featured-image.png.jpg")
    id = models.BigIntegerField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title

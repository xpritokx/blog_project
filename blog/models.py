from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Article(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    summary = RichTextUploadingField(blank=True, default="")
    content = RichTextUploadingField(blank=True, default="")

    def __str__(self):
        return  self.title

    class Meta:
        ordering = ["-time"]
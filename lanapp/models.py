from django.db import models
from django.urls import reverse
# Create your models here.
class Malumot(models.Model):
    class Meta:
        verbose_name = 'Malumot'
        verbose_name_plural = 'Malumotlar'


    first_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    text = models.TextField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("lanapp:malumot", kwargs={'slug': self.slug})
    
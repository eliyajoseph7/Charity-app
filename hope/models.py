from django.db import models
from django.utils.text import slugify

class Contact(models.Model):
    name        = models.CharField(max_length=255)
    email       = models.EmailField(max_length=254)
    subject     = models.CharField(max_length=50)
    message     = models.TextField()
    slug        = models.SlugField(max_length=140, unique=True, blank=True)
    date        = models.DateTimeField(blank=True, auto_now_add=True, null=True)

    def __str__(self):
        return self.subject

    def get_unique_slug(self):
        slug = slugify(self.subject)  
        unique_slug = slug

        num = 1
        while Contact.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)

            num += 1

        return unique_slug


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        super().save(*args, **kwargs)

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


class Portfolio(models.Model):
    HOSP    =  'hospital'
    ORPH   =  'orphanage'
    PRIS     =  'prisons'
    DRU =  'drug_addiction'

    CATEGORY_SELECT = [
        (HOSP, 'Hospital'),
        (ORPH, 'Orphanage'),
        (PRIS, 'Prisons'),
        (DRU, 'Drug addiction center')
    ]
    

    title           =   models.CharField(max_length=225)
    description     =   models.TextField()
    category        =   models.CharField(choices=CATEGORY_SELECT, max_length=20)
    date            =   models.DateField(auto_now_add=True)
    img_url         =   models.URLField(max_length=2000)
    slug            =   models.SlugField(max_length=140, unique=True, blank=True)


    def __str__(self):
        return self.title
    
    def get_unique_slug(self):
        slug    =   slugify(self.title)
        unigue_slug =   slug

        num = 1
        while Portfolio.objects.filter(slug=unigue_slug).exists():
            unigue_slug = '{}_{}'.format(slug, num)

            num += 1

        return unigue_slug


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        super().save(*args, **kwargs)       

        
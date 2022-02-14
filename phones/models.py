from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField()
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return f"{self.name}, {self.slug}"

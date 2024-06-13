from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
 
# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=90)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}, code = {self.code}"
    
    class Meta:
        verbose_name_plural = "Contries"


class Address(models.Model):
    street = models.CharField(max_length=90)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.city}, {self.street}, {self.zip_code}"
    
    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    published_Countries = models.ManyToManyField(Country)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save( *args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("single_book", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"

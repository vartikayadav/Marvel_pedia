from django.db import models

# Create your models here.
class Comics(models.Model):
    title=models.CharField(max_length=256)
    published=models.DateField(null=True)
    slug=models.SlugField(max_length=256,unique=True,null=True)
    Penciller=models.CharField(max_length=256,null=True)
    description=models.TextField(null=True,blank=True)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField(null=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        ordering=['title']
        verbose_name='comic'
        verbose_name_plural='comics'

    def __str__(self):
        return self.title

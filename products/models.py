from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at=models.DateField(auto_created=True)
    updated_at=models.DateField(auto_created=True)

    class Meta:
        abstract=True #Django will treat BaseModel as a class and not as a Model.

class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    product_slug=models.SlugField(unique=True)
    product_description=models.TextField()
    product_price=models.IntegerField(default=0)
    product_demo_price=models.IntegerField(default=0)
    quantity=models.CharField(null=True,blank=True)

class ProductMetaInformation(BaseModel):
    product=models.OneToOneField(Product,on_delete=models.CASCADE)
    measuring_unit=models.CharField(max_length=100,null=True,blank=True, choices=(("kg","kg"),("l","l"),("ml","ml"),(None,None)))
    quantity=models.CharField(null=True,blank=True)
    
class ProductIimage(BaseModel):
    product_image=models.ImageField(upload_to="products")

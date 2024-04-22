from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


    
class ProductImages(models.Model):
    image = models.ImageField(upload_to='product/images', db_index=True, default=None)


class Product(models.Model):
    
    images = models.ManyToManyField(ProductImages, db_index=True, default=None)
    product_slug = models.SlugField(db_index=True, default="")
    title = models.CharField(max_length=100, db_index=True, default="")
    product_description = models.TextField(db_index=True, default="")
    Date_created = models.DateField(auto_now_add = True)
    orignal_price = models.PositiveIntegerField(db_index=True, default=0)
    tax_price = models.PositiveIntegerField(db_index=True, default=0, null=True)
    delivery_price = models.PositiveIntegerField(db_index=True, default=0, null=True)
    tag = models.CharField(max_length=50, default="")
    stock_quantity = models.PositiveIntegerField(db_index=True, default=1, null=True)

    published = models.BooleanField(default=True)

class Address(models.Model):

    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE, null=True, related_name="useraddress")
    first_name = models.CharField(max_length=100, db_index=True, default="")
    last_name = models.CharField(max_length=100, db_index=True, default="")
    phone_no = models.BigIntegerField(db_index=True)
    state = models.CharField(max_length=100, db_index=True, default="")
    city = models.CharField(max_length=100, db_index=True, default="")
    street_no = models.CharField(max_length=300, db_index=True, default="")
    postal_code = models.CharField(max_length=100, db_index=True, default="")





class Orders(models.Model):
    STATUS = (
        ("Cancel", "Cancel"),
        ("Delivered", "Delivered"),
        ("Return", "Return"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    order_id = models.CharField(max_length=100, db_index = True,  default="")
    products = models.ManyToManyField(Product, db_index=True, default="")
    status = models.CharField(max_length=100,  choices=STATUS, db_index = True,  default="")
    total_price = models.PositiveIntegerField(db_index = True)
    quatity = models.PositiveIntegerField(db_index=True)
    date_created = models.DateField(auto_now_add = True)
    date_cancel = models.DateField(auto_now_add = True, null=True)
    date_return = models.DateField(auto_now_add = True, null=True)

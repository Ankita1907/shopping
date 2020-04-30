from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category =models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    contact_id = models.AutoField
    contact_name = models.CharField(max_length=50)
    contact_no = models.IntegerField(default=0)
    contact_email = models.EmailField('User Email')
    contact_post = models.CharField(max_length=50)
    Contact_about = models.TextField()
    contact_image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.contact_name



class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    zip_code =models.CharField(max_length=500)




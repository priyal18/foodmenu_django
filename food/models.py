from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete = models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=400)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default = " https://img.etimg.com/thumb/msid-65511444,width-643,imgsize-487093,resizemode-4/food-eat-bbq-meat-gettyimages-673139382.jpg ")

    def get_absolute_url(self):
        return reverse("food:detail",kwargs={"pk":self.pk})

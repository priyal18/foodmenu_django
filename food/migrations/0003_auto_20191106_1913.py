# Generated by Django 2.2.4 on 2019-11-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default=' https://i2.wp.com/flavouroma.com/wp-content/uploads/2017/05/veg-pizza-recipe-healthy.jpg?w=840&ssl=1 ', max_length=500),
        ),
    ]

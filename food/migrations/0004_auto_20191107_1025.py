# Generated by Django 2.2.4 on 2019-11-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20191106_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default=' https://image.flaticon.com/icons/svg/1377/1377194.svg ', max_length=500),
        ),
    ]

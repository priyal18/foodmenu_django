# Generated by Django 2.2.4 on 2019-11-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default=' https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.paramfood.in%2Fwp-content%2Fuploads%2F2016%2F02%2FSuper-Veg.-Pizza.jpg&imgrefurl=http%3A%2F%2Fwww.paramfood.in%2Fproduct%2Fsuper-veg-pizza%2F&docid=5ytuzp-upVmyEM&tbnid=WhZu8hZ520v41M%3A&vet=10ahUKEwju7r-FmNblAhUZk3AKHawUDZsQMwiDASgJMAk..i&w=852&h=850&bih=620&biw=1366&q=veg%20Pizza&ved=0ahUKEwju7r-FmNblAhUZk3AKHawUDZsQMwiDASgJMAk&iact=mrc&uact=8 ', max_length=500),
        ),
    ]

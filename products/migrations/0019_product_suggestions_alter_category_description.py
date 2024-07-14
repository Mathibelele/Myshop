# Generated by Django 5.0.6 on 2024-06-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='suggestions',
            field=models.ManyToManyField(to='products.product'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.0.5 on 2023-01-10 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_abstractdetailuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AbstractDetailUser',
        ),
    ]
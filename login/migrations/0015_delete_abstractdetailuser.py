# Generated by Django 4.0.5 on 2023-01-10 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_abstractdetailuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AbstractDetailUser',
        ),
    ]
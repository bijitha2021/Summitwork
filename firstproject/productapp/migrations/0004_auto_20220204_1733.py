# Generated by Django 3.2.8 on 2022-02-04 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='Product',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]

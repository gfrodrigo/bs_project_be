# Generated by Django 5.0.3 on 2024-04-03 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_item_tax_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Business',
        ),
    ]

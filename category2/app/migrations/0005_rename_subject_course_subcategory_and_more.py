# Generated by Django 4.1.7 on 2023-03-13 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_subcategory_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='subject',
            new_name='subcategory',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='subject',
            new_name='subcategory',
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-14 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_topic_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course'),
        ),
    ]

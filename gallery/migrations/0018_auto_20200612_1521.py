# Generated by Django 3.0.6 on 2020-06-12 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0017_auto_20200612_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.Gallery'),
        ),
    ]

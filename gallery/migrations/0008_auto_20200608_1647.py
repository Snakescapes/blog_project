# Generated by Django 3.0.6 on 2020-06-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20200608_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='<django.db.models.fields.related.ForeignKey><function get_filename at 0x03BB3D60>'),
        ),
    ]

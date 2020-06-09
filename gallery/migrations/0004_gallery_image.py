# Generated by Django 3.0.6 on 2020-06-08 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0006_auto_20200608_1455'),
        ('gallery', '0003_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(default='default.jpg', upload_to='gallery')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-02 00:54

from django.db import migrations, models
import django.db.models.deletion
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dates', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AdventurePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to=gallery.models.make_pic_path)),
                ('picture_desc', models.CharField(max_length=200)),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.adventure')),
            ],
        ),
    ]

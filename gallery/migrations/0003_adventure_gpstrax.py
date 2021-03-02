# Generated by Django 3.1.5 on 2021-02-28 06:47

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_adventurepicture_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventure',
            name='gpstrax',
            field=models.FileField(blank=True, upload_to=gallery.models.make_gps_path),
        ),
    ]

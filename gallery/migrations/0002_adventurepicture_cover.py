# Generated by Django 3.1.5 on 2021-02-02 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventurepicture',
            name='cover',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-02 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0003_guestbookentry_entry_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbookentry',
            name='entry_picture',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
